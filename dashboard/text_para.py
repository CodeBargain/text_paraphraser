import streamlit as st
from src.paraphraser import supported_langs, paraphrase

st.markdown("""<h3 style='text-align: center; color: grey;'>Text paraphraser</h3>""", unsafe_allow_html=True)

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
    default_text = """Paraphrasing text using AI involves leveraging advanced natural language processing (NLP) techniques to rephrase sentences or passages while retaining their original meaning. AI-powered paraphrasing systems utilize large language models trained on diverse textual data to generate alternative phrasings that maintain coherence and context. These systems analyze the input text's structure, semantics, and relationships between words to produce high-quality paraphrased output. This technology finds applications in content creation, language translation, and improving the readability of complex text. By harnessing AI for paraphrasing, users can efficiently transform and enhance their written content, achieving greater clarity and engagement while preserving the intended message."""
    with st.sidebar:
        input_text = st.text_area("Input Text", height = 100, value = default_text)
        if not input_text:
            st.error('Please enter some text')
        selected_lang = st.selectbox("Language Selection", supported_langs)
        selected_mode = st.selectbox("Paraphrasing Mode", mode_name)
        submit_button = st.form_submit_button("Submit")

if submit_button and len(input_text) != 0:
    mystyle = """
    <style>
        p {
            text-align: justify;
        }
    </style>
    """
    paraphrase_result = paraphrase(text=input_text, mode = mode[selected_mode], lang=supported_langs[selected_lang])
    paraphrase_markdown = f"{mystyle}\n{paraphrase_result}"
    st.markdown(paraphrase_markdown, unsafe_allow_html = True)