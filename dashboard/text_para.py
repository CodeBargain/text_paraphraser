import streamlit as st
from src.paraphraser import supported_langs, paraphrase

st.markdown("<h2 style='text-align: center; color: grey;'>Text paraphraser</h2>", unsafe_allow_html=True)
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

mode = {
    "Fluency": 1,
    "Standard":2
}
mode_name = [str(mode_name) for mode_name in mode.keys()]

with st.form("paraphrase_form"):
    with st.sidebar:
        input_text = st.text_area("Enter your text here: ", height = 100)
        selected_lang = st.selectbox("Select paraphrase language: ", supported_langs)
        selected_mode = st.selectbox("Select mode", mode_name)
        submit_button = st.form_submit_button("Submit")

if submit_button and len(input_text) != 0:
    # st.markdown("<h2> style = 'text-align: justify")
    mystyle = """
    <style>
        p {
            text-align: justify;
        }
    </style>
    """
    paraphrase_result = paraphrase(text=input_text, mode = mode[selected_mode], lang=supported_langs[selected_lang])
    st.markdown(mystyle, unsafe_allow_html=True)
    st.write(paraphrase_result)