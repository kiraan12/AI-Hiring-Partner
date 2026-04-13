"""
TalentScout UI Components
Custom CSS, layout helpers, sidebar rendering, and chat bubble rendering.
"""

import re
import html
import streamlit as st


def apply_custom_css():
    """Inject custom CSS for the TalentScout dark-themed UI."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Syne:wght@600;700;800&display=swap');

        :root {
            --bg-primary: #0a0f1e;
            --bg-secondary: #111827;
            --bg-card: #161d2f;
            --accent-blue: #3b82f6;
            --accent-cyan: #06b6d4;
            --accent-emerald: #10b981;
            --accent-amber: #f59e0b;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --text-muted: #475569;
            --border: #1e293b;
            --user-bubble: #1e3a5f;
            --bot-bubble: #161d2f;
            --gradient: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
        }

        .stApp {
            background-color: var(--bg-primary) !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        .main .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            max-width: 860px !important;
        }

        /* ── Header ── */
        .ts-header {
            text-align: center;
            padding: 1.5rem 0 1.2rem;
            border-bottom: 1px solid var(--border);
            margin-bottom: 1.5rem;
        }
        .ts-logo {
            font-family: 'Syne', sans-serif;
            font-size: 1.9rem;
            font-weight: 800;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .ts-tagline {
            color: var(--text-secondary);
            font-size: 0.88rem;
            margin-top: 0.2rem;
        }
        .ts-badge {
            display: inline-block;
            background: rgba(59,130,246,0.15);
            border: 1px solid rgba(59,130,246,0.3);
            color: var(--accent-blue);
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.18rem 0.55rem;
            border-radius: 999px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
        }

        /* ── Chat bubbles ── */
        .chat-wrap {
            display: flex;
            gap: 0.65rem;
            margin-bottom: 0.9rem;
            align-items: flex-start;
            animation: fadeUp 0.25s ease-out;
        }
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(6px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .chat-wrap.user { flex-direction: row-reverse; }

        .chat-avatar {
            width: 34px; height: 34px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.95rem; flex-shrink: 0; margin-top: 3px;
        }
        .chat-avatar.bot  { background: var(--gradient); }
        .chat-avatar.user { background: #1e3a5f; border: 1px solid rgba(59,130,246,0.4); }

        .chat-bubble {
            max-width: 76%;
            padding: 0.8rem 1rem;
            border-radius: 16px;
            font-size: 0.91rem;
            line-height: 1.65;
            color: var(--text-primary);
            white-space: normal;
            overflow-wrap: anywhere;
            word-break: break-word;
        }
        .chat-bubble.bot {
            background: var(--bot-bubble);
            border: 1px solid var(--border);
            border-top-left-radius: 4px;
        }
        .chat-bubble.user {
            background: var(--user-bubble);
            border: 1px solid rgba(59,130,246,0.25);
            border-top-right-radius: 4px;
        }
        .chat-bubble strong { color: var(--accent-cyan); }
        .chat-bubble hr { border-color: var(--border); margin: 0.4rem 0; }
        .chat-bubble code {
            background: rgba(255,255,255,0.07);
            padding: 0.1rem 0.35rem;
            border-radius: 4px;
            font-size: 0.85em;
        }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background-color: var(--bg-secondary) !important;
            border-right: 1px solid var(--border) !important;
        }
        .sidebar-section {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 0.9rem;
            margin-bottom: 0.9rem;
        }
        .sidebar-title {
            font-family: 'Syne', sans-serif;
            font-size: 0.7rem;
            font-weight: 700;
            color: var(--accent-blue);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.65rem;
        }
        .info-label {
            font-size: 0.66rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 600;
        }
        .info-value {
            font-size: 0.83rem;
            color: var(--text-primary);
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        .tech-pill {
            display: inline-block;
            background: rgba(6,182,212,0.12);
            border: 1px solid rgba(6,182,212,0.3);
            color: var(--accent-cyan);
            font-size: 0.7rem;
            font-weight: 600;
            padding: 0.15rem 0.5rem;
            border-radius: 999px;
            margin: 0.15rem 0.1rem;
        }
        .progress-item {
            display: flex; align-items: center; gap: 0.45rem;
            margin-bottom: 0.35rem;
            font-size: 0.8rem;
            color: var(--text-secondary);
        }
        .dot-done    { width:8px;height:8px;border-radius:50%;background:var(--accent-emerald);flex-shrink:0; }
        .dot-pending { width:8px;height:8px;border-radius:50%;background:var(--text-muted);flex-shrink:0; }

        /* ── Privacy banner ── */
        .privacy-banner {
            background: rgba(245,158,11,0.08);
            border: 1px solid rgba(245,158,11,0.25);
            border-radius: 8px;
            padding: 0.6rem 0.85rem;
            font-size: 0.75rem;
            color: var(--accent-amber);
            margin-bottom: 0.9rem;
            line-height: 1.5;
        }

        /* ── Input ── */
        .stChatInput > div {
            background: var(--bg-card) !important;
            border: 1px solid var(--border) !important;
            border-radius: 12px !important;
        }
        .stChatInput textarea {
            color: var(--text-primary) !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        /* ── Button ── */
        .stButton > button {
            background: var(--gradient) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
        }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: var(--bg-primary); }
        ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    """Render the top header bar."""
    st.markdown(
        """
        <div class="ts-header">
            <div class="ts-badge">🤖 Powered by Mistral-7B · HuggingFace</div>
            <div class="ts-logo">🎯 TalentScout</div>
            <div class="ts-tagline">AI-Powered Technical Hiring Assistant</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chat_message(role: str, content: str):
    """Render a single chat message using Streamlit native chat UI."""
    chat_role = "assistant" if role == "assistant" else "user"
    avatar = "🎯" if role == "assistant" else "👤"
    with st.chat_message(chat_role, avatar=avatar):
        st.markdown(content)


def _md_to_html(text: str) -> str:
    """Minimal Markdown → HTML conversion for chat bubbles."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = text.replace("---", "<hr>")
    text = text.replace("\n\n", "<br><br>").replace("\n", "<br>")
    text = re.sub(r"(\d+)\.\s", r"<br>\1. ", text)
    return text


def render_sidebar(candidate_info: dict):
    """Render the sidebar with live candidate profile, tech stack, and progress."""
    with st.sidebar:
        st.markdown(
            "<div style='font-family:Syne,sans-serif;font-size:1.1rem;font-weight:800;"
            "color:#f1f5f9;margin-bottom:1rem;'>Candidate Profile</div>",
            unsafe_allow_html=True,
        )

        # ── Privacy Notice ───────────────────────────────────────────────────
        st.markdown(
            '<div class="privacy-banner">'
            "🔐 <strong>Data Privacy</strong><br>"
            "Your data is used solely for this screening session and is not shared with third parties. "
            "Sensitive fields are pseudonymised in storage."
            "</div>",
            unsafe_allow_html=True,
        )

        # ── Basic Info ───────────────────────────────────────────────────────
        info_fields = [
            ("full_name", "Full Name"),
            ("email", "Email"),
            ("phone", "Phone"),
            ("years_of_experience", "Experience"),
            ("desired_position", "Desired Role"),
            ("current_location", "Location"),
        ]
        has_info = any(f[0] in candidate_info for f in info_fields)

        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">📋 Basic Info</div>', unsafe_allow_html=True)
        if not has_info:
            st.markdown(
                "<span style='color:#475569;font-size:0.8rem;'>Waiting for responses...</span>",
                unsafe_allow_html=True,
            )
        else:
            for key, label in info_fields:
                if key in candidate_info:
                    st.markdown(
                        f'<div class="info-label">{label}</div>'
                        f'<div class="info-value">{candidate_info[key]}</div>',
                        unsafe_allow_html=True,
                    )
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Tech Stack ───────────────────────────────────────────────────────
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">💻 Tech Stack</div>', unsafe_allow_html=True)
        tech_stack = candidate_info.get("tech_stack")
        if tech_stack:
            pills = "".join(f'<span class="tech-pill">{t}</span>' for t in tech_stack)
            st.markdown(pills, unsafe_allow_html=True)
        else:
            st.markdown(
                "<span style='color:#475569;font-size:0.8rem;'>Not declared yet</span>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Progress Tracker ─────────────────────────────────────────────────
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">✅ Progress</div>', unsafe_allow_html=True)
        steps = [
            ("full_name" in candidate_info or "email" in candidate_info, "Personal Info"),
            ("tech_stack" in candidate_info, "Tech Stack Declared"),
            (
                "tech_stack" in candidate_info and len(candidate_info.get("tech_stack", [])) > 0,
                "Technical Questions",
            ),
        ]
        for done, label in steps:
            dot = "dot-done" if done else "dot-pending"
            st.markdown(
                f'<div class="progress-item"><div class="{dot}"></div>{label}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Footer ───────────────────────────────────────────────────────────
        st.markdown(
            "<div style='color:#334155;font-size:0.7rem;text-align:center;margin-top:1rem;'>"
            "© 2025 TalentScout · All rights reserved</div>",
            unsafe_allow_html=True,
        )
