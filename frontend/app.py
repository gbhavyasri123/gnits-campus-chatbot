import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
from chatbot.engine import ask_question

st.set_page_config(
    page_title="GNITS Campus Chatbot",
    page_icon="🎓",
    layout="wide"
)

# ---------- Custom CSS ----------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.big-title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1E3A8A;
}

.sub-title {
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

.answer-box {
    background-color:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}

.stButton>button {
    width:100%;
    background-color:#1E3A8A;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
}

.stTextInput>div>div>input {
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------

st.markdown(
    '<p class="big-title">🎓 GNITS Campus Chatbot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI Powered Assistant for Students, Faculty and Visitors</p>',
    unsafe_allow_html=True
)

# ---------- Sidebar ----------

st.sidebar.title("📌 Quick Questions")

sample_questions = [
    "What facilities are available in GNITS?",
    "Tell me about placements",
    "What departments are available?",
    "What hostel facilities are provided?",
    "What clubs are available?"
]

for q in sample_questions:
    if st.sidebar.button(q):
        st.session_state["question"] = q

# ---------- Input ----------

query = st.text_input(
    "Ask Anything About GNITS",
    value=st.session_state.get("question", "")
)

# ---------- Ask ----------

if st.button("🚀 Ask GNITS Bot"):

    if query:

        with st.spinner("Searching GNITS Knowledge Base..."):

            answer = ask_question(query)

        st.markdown("### 🤖 Answer")

        st.markdown(
            f"""
            <div class="answer-box">
            {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------- Footer ----------

st.markdown("---")
st.caption("Developed using Streamlit • HuggingFace • FAISS • LangChain • Gemini")