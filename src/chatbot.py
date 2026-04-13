import json
import re
import os
from typing import Tuple
from dotenv import load_dotenv
from groq import Groq

# ─── LOAD ENV ─────────────────────────────────────────

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ─── INIT CLIENT ──────────────────────────────────────

client = Groq(api_key=GROQ_API_KEY)

# ─── CONSTANTS ────────────────────────────────────────

EXIT_KEYWORDS = {"exit", "quit", "bye", "goodbye", "stop", "end"}

# ─── SYSTEM PROMPT (FULL MASTER PROMPT) ───────────────

SYSTEM_PROMPT = """
You are an AI Hiring Assistant for a recruitment agency called "TalentScout".

========================================
🎯 OBJECTIVE
========================================
Conduct a structured candidate screening.

========================================
🧩 PHASES (STRICT)
========================================
PHASE 1: INFORMATION GATHERING  
PHASE 2: TECHNICAL QUESTIONS  
PHASE 3: WRAP-UP  

You MUST follow order. Do NOT skip.

----------------------------------------
PHASE 1: COLLECT (ONE BY ONE)
----------------------------------------
1. Full Name  
2. Email  
3. Phone  
4. Experience  
5. Desired Role  
6. Location  
7. Tech Stack  

Rules:
- Ask ONE question at a time
- Do NOT repeat questions
- Wait for user input

----------------------------------------
📌 DATA EXTRACTION
----------------------------------------
When user gives valid data, append:

<<<CANDIDATE_DATA>>>
{
  "field": "value"
}
<<<END_DATA>>>

----------------------------------------
✅ VALIDATION
----------------------------------------
- Email must contain @ and .
- Phone must be numeric (10+ digits)
- Experience must be number

----------------------------------------
PHASE 2: TECH QUESTIONS
----------------------------------------
After ALL data collected:

- Extract technologies
- For EACH tech:
  - Generate 3–5 questions
  - Beginner → Advanced
  - Real-world based
  - NO answers

FORMAT:

Technology: Python
1. Question
2. Question

----------------------------------------
PHASE 3: END
----------------------------------------
Say:
"Thank you for your details. Our team will contact you."

----------------------------------------
🧯 FALLBACK
----------------------------------------
If unclear:
"I'm here to assist with hiring. Please provide the requested information."

----------------------------------------
🛑 EXIT
----------------------------------------
If user says exit/quit:
"Thank you for your time. Our team will get back to you soon."

----------------------------------------
🚀 START
----------------------------------------
Start with:
"Hello! Welcome to TalentScout 🤝  
Let’s begin — what is your full name?"
"""

# ─── CLASS ───────────────────────────────────────────

class TalentScoutBot:

    def get_greeting(self):
        return (
            "👋 Welcome to TalentScout AI Hiring Assistant!\n\n"
            "Let’s start — could you please tell me your full name?"
        )

    def get_farewell(self):
        return "Thank you for your time. Our team will get back to you soon."

    def is_exit_keyword(self, text: str) -> bool:
        return text.lower().strip() in EXIT_KEYWORDS

    # ─── DATA EXTRACTION ─────────────────────────────

    def _extract_candidate_data(self, text: str) -> dict:
        pattern = r"<<<CANDIDATE_DATA>>>([\s\S]*?)<<<END_DATA>>>"
        match = re.search(pattern, text)

        if not match:
            return {}

        try:
            data = json.loads(match.group(1).strip())
            return {k: v for k, v in data.items() if v is not None}
        except:
            return {}

    def _clean_response(self, text: str) -> str:
        pattern = r"<<<CANDIDATE_DATA>>>[\s\S]*?<<<END_DATA>>>"
        return re.sub(pattern, "", text).strip()

    # ─── MAIN CHAT ───────────────────────────────────

    def chat(self, user_message: str, history: list) -> Tuple[str, dict]:

        if self.is_exit_keyword(user_message):
            return self.get_farewell(), {}

        if not GROQ_API_KEY:
            return ("⚠️ GROQ_API_KEY not set in .env file.", {})

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for msg in history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            raw = completion.choices[0].message.content

            clean = self._clean_response(raw)
            data = self._extract_candidate_data(raw)

            return clean, data

        except Exception as e:
            return (f"⚠️ Error: {str(e)}", {})