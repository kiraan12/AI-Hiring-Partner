# 🤖 TalentScout AI Hiring Assistant

An intelligent AI-powered chatbot designed to streamline the initial screening process for technical candidates. Built using modern LLM integration and a clean user interface, this system simulates a real-world hiring assistant used by recruitment agencies.

---

## 🚀 Project Overview

**TalentScout Hiring Assistant** is an AI chatbot that conducts structured candidate screening by:

* Collecting essential candidate details
* Understanding the candidate’s tech stack
* Generating relevant technical questions
* Maintaining contextual conversation flow

This project demonstrates practical application of **LLMs, prompt engineering, and conversational AI design** in a recruitment scenario.

---

## 🎯 Key Features

### 🧾 Structured Candidate Screening

* Collects:

  * Full Name
  * Email Address
  * Phone Number
  * Years of Experience
  * Desired Role
  * Location
  * Tech Stack

---

### 🧠 Intelligent Question Generation

* Dynamically generates **3–5 technical questions per technology**
* Covers:

  * Beginner → Intermediate → Advanced levels
  * Real-world problem scenarios

---

### 💬 Context-Aware Chatbot

* Maintains conversation state
* Handles follow-up responses intelligently
* Ensures smooth multi-step interaction

---

### 🛡️ Robust Input Handling

* Input validation (email, phone, experience)
* Fallback responses for unclear inputs
* Exit command handling (`exit`, `quit`, `bye`)

---

### 📊 Structured Data Extraction

* Extracts candidate data in JSON format:

```json
{
  "full_name": "Kiran R",
  "experience": "2 years"
}
```

---

### 🎨 Professional UI

* Built with **Streamlit**
* Chat-style interface
* Clean and modern design for better user experience

---

## 🛠️ Tech Stack

| Component     | Technology Used          |
| ------------- | ------------------------ |
| Frontend UI   | Streamlit                |
| Backend Logic | Python                   |
| LLM API       | Groq (LLaMA 3.1)         |
| Prompt Design | Custom Structured Prompt |
| Data Handling | JSON Extraction          |
| Environment   | Python + dotenv          |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/talentscout-chatbot.git
cd talentscout-chatbot
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Prompt Engineering Strategy

The chatbot is powered by a **structured master prompt** designed to:

* Enforce strict conversation phases:

  * Information Gathering
  * Technical Evaluation
  * Wrap-up

* Ensure:

  * One question at a time
  * No deviation from hiring context
  * Accurate and relevant question generation

* Enable **LLM-guided structured data extraction** using delimiters:

```
<<<CANDIDATE_DATA>>>
{ ... }
<<<END_DATA>>>
```

---

## 🏗️ System Architecture

```
User (Streamlit UI)
        ↓
Chat Interface (app.py)
        ↓
Chatbot Logic (chatbot.py)
        ↓
LLM API (Groq - LLaMA 3.1)
        ↓
Response Processing + JSON Extraction
```

---

## ⚠️ Challenges & Solutions

### 🔹 Challenge: Running LLM Locally

* Local LLaMA required heavy resources
* **Solution:** Switched to Groq API for fast and reliable inference

---

### 🔹 Challenge: Maintaining Conversation Flow

* LLMs can skip steps or hallucinate
* **Solution:** Designed strict phase-based prompt

---

### 🔹 Challenge: Structured Data Extraction

* Extracting clean JSON from responses
* **Solution:** Used delimiter-based parsing system

---

## 🔐 Data Privacy Considerations

* No real user data is stored
* Uses simulated/local session data
* API keys are secured using `.env`
* Follows best practices aligned with GDPR principles

---

## 🎥 Demo

> A short walkthrough video demonstrating:

* Candidate interaction
* Data collection
* Technical question generation

*(Attach Loom / screen recording link here)*

---

## 🚀 Future Enhancements

* Candidate scoring system
* Resume parsing integration
* Multi-language support
* Recruiter dashboard
* Database integration

---

## 👨‍💻 Author

**Kiran R**
AI/ML Enthusiast | Data Science | NLP

---

## ⭐ Final Note

This project reflects a real-world application of AI in recruitment workflows, combining **LLM capabilities, prompt engineering, and user-focused design** to deliver a scalable hiring assistant solution.

---
