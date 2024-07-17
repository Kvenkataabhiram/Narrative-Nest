import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()   
# Set your API key directly as an environment variable
os.environ["GOOGLE_API_KEY"] = "AIzaSyDSvSN87YizAHtqClnGBYInlwpVQL7CQ2I"

# Configure GenerativeAI with the API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


def getResponse(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


st.set_page_config(page_title="GenHub", page_icon="📑", layout='centered', initial_sidebar_state='collapsed')
st.header("NarrativeNest 📑")

input_text = st.text_input("Enter the Topic")
col1, col2 = st.columns([5, 5])
col3, col4 = st.columns([5, 5])
with col1:
    style = st.selectbox('Content type', ('story', 'poem', 'essay', 'role play', 'blog'))
with col2:
    for_whom = st.selectbox('Writing the content for', ('Researchers', 'Engineer', 'Student', 'Professor', 'Common People'), index=0)
with col3:
    number = st.text_input('No of lines/words')
with col4:
    ln = st.selectbox('Content in specified', ('words', 'lines', 'paragraphs'))

submit = st.button("Generate")

if submit:
    prompt = f"Write a {style} for {for_whom} on the topic {input_text} within {number} {ln}."
    response = getResponse(prompt)
    st.write(response.replace('\n', '\n\n'))