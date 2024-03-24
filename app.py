import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
st.set_page_config(page_title="MathScripter", layout="wide")

def backend(text):
    model = genai.GenerativeModel('gemini-pro')
    st.session_state['response']["solution"] = model.generate_content(f"You are a Mathematician. Solve the problem statement - {text}").text
    st.session_state['response']["python"] = model.generate_content(f"You are a Programmer. Write a python script for the problem statement without any explanation - {text}").text
    st.session_state['response']["matlab"] = model.generate_content(f"You are a Programmer. Write a matlab script for the problem statement without any explanation - {text}").text
    st.session_state['response']["script"] = st.session_state['response']["python"]

def toggle_script(key):
    st.session_state['response']["script"] = st.session_state['response'][key]

if 'response' not in st.session_state:
    st.session_state['response'] = {"solution":"", "script":"", "python":"", "matlab":""}

header = st.container()
body = st.container()

with header:
    st.markdown("<h1 style='text-align: center;'>MathScripter</h1>", unsafe_allow_html=True)
    st.subheader('', divider='gray')

with body:

    input = st.container()
    output = st.container()

    with input:
        text = st.text_area("Enter the Problem Statement")
        st.button('Submit', on_click = backend, args=(text,))

    with output:
        out_1, out_2 = st.columns(2)
        with out_1:
            st.subheader("Solution", divider=False)
            st.markdown(st.session_state['response']["solution"])
        with out_2:
            st.subheader("Script", divider=False)
            col_1, col_2, *_ = st.columns(6)
            with col_1:
                st.button("Python", on_click = toggle_script, args=("python",))
            with col_2:
                st.button("Matlab", on_click = toggle_script, args=("matlab",))
            st.markdown(st.session_state['response']["script"])
