# 🤖 DSA AI Mentor

An AI-powered DSA learning assistant built with LangGraph, Groq (Llama 3.1), and Streamlit.

---

## Features
- **Explain DSA Topics** — Step-by-step explanations in simple language with small examples
- **Generate Problems** — Creates LeetCode-style problems for any topic and difficulty (Easy, Medium, Hard)
- **Hints** — Provides small hints without giving the full solution
- **Code Evaluation** — Checks user-submitted code for correctness, time complexity, and better approaches
- **Interactive UI** — Easy to use with Streamlit interface
- **Follow-up Guidance** — Suggests next steps and optimizations

---

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/dsa-ai-mentor.git
cd dsa-ai-mentor

Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Add your Groq API key to .env:

GROQ_API_KEY=your_key_here

Run the app:

streamlit run frontend.py
How to Use

Explain Topic — Enter a DSA topic and click Explain to get a step-by-step explanation.

Generate Problem — Enter a topic, select difficulty, and click Generate to receive a LeetCode-style problem.

Get Hint — Paste a problem and click Get Hint to receive a helpful hint.

Evaluate Code — Paste the problem and your solution, click Evaluate, and get feedback on correctness, time complexity, and improvements.

Tech Stack

LangGraph — Agent orchestration and memory management

Groq (Llama 3.1 8B) — Fast AI inference for explanations and problem generation

Streamlit — Interactive web user interface

Pandas — Handles data processing if needed

Notes

Keep your .env file private — do not push your Groq API key to GitHub.

Designed for beginners to intermediate learners in DSA.

Use the generated problems for practice on your local environment or online platforms like LeetCode.
