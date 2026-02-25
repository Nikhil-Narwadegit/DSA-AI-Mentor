import streamlit as st
from mentor import explain_topic, generate_problem, give_hint, evaluate_code

st.set_page_config(page_title="DSA AI Mentor", layout="centered")
st.title("🤖 DSA AI Mentor")

# Keep menu and results in session_state
if "menu" not in st.session_state:
    st.session_state.menu = "Explain Topic"
if "result" not in st.session_state:
    st.session_state.result = ""
if "problem_text" not in st.session_state:
    st.session_state.problem_text = ""
if "code_text" not in st.session_state:
    st.session_state.code_text = ""

menu = st.sidebar.selectbox(
    "Choose Mode",
    ["Explain Topic", "Generate Problem", "Get Hint", "Evaluate Code"],
    index=["Explain Topic", "Generate Problem", "Get Hint", "Evaluate Code"].index(st.session_state.menu),
    key="menu_select"
)

st.session_state.menu = menu  # keep current menu in session

# --- EXPLAIN TOPIC ---
if menu == "Explain Topic":
    topic = st.text_input("Enter DSA Topic", key="topic_input")
    if st.button("Explain"):
        if topic:
            with st.spinner("Teaching..."):
                st.session_state.result = explain_topic(topic)
    if st.session_state.result:
        st.write(st.session_state.result)

# --- GENERATE PROBLEM ---
elif menu == "Generate Problem":
    topic = st.text_input("Enter Topic for Problem", key="topic_problem")
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"], key="difficulty_select")
    
    if st.button("Generate"):
        if topic:
            with st.spinner("Creating problem..."):
                st.session_state.result = generate_problem(f"{difficulty} {topic}")
                st.session_state.problem_text = st.session_state.result
                st.session_state.hint_result = ""  # reset previous hint

    if "result" in st.session_state and st.session_state.result:
        st.text_area("Problem", st.session_state.result, height=300, key="problem_area")

        # Inline "Get Hint" button
        if st.button("Get Hint for this problem"):
            if st.session_state.problem_text:
                with st.spinner("Thinking..."):
                    st.session_state.hint_result = give_hint(st.session_state.problem_text)
        if "hint_result" in st.session_state and st.session_state.hint_result:
            st.write("💡 Hint:")
            st.write(st.session_state.hint_result)

        # Inline code submission box
        st.write("💻 Submit Your Code")
        code_input = st.text_area("Paste Your Solution Here", height=200, key="code_input")

        # Evaluate button
        if st.button("Check Code"):
            if st.session_state.problem_text and code_input:
                with st.spinner("Checking code..."):
                    eval_result = evaluate_code(st.session_state.problem_text, code_input)
                st.write("✅ Evaluation Result:")
                st.write(eval_result)

# --- GET HINT ---
elif menu == "Get Hint":
    problem = st.text_area("Paste Problem", value=st.session_state.problem_text, height=300, key="hint_problem")
    if st.button("Get Hint"):
        if problem:
            with st.spinner("Thinking..."):
                st.session_state.result = give_hint(problem)
    if st.session_state.result:
        st.write(st.session_state.result)

# --- EVALUATE CODE ---
elif menu == "Evaluate Code":
    problem = st.text_area("Paste Problem", value=st.session_state.problem_text, height=200, key="eval_problem")
    code = st.text_area("Paste Your Code", value=st.session_state.code_text, height=200, key="eval_code")
    if st.button("Evaluate"):
        if problem and code:
            with st.spinner("Checking code..."):
                st.session_state.result = evaluate_code(problem, code)
                st.session_state.problem_text = problem
                st.session_state.code_text = code
    if st.session_state.result:
        st.write(st.session_state.result)
