
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai
auth_token = st.secrets["auth_token"]
#'AIzaSyCSw4QYFCuQPLefm8eklclNzw6IpkUm2IA'
genai.configure(api_key=auth_token)

## Function to load OpenAI model and get respones
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app
st.set_page_config(page_title="GeminiPro Clone")
st.header("Gemini Captioning Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image You Uploaded.", use_column_width=True)

#Button
submit=st.button("Explain this Image")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
