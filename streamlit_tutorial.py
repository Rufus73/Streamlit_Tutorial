import streamlit as st
import os
from dotenv import load_dotenv
from langchain.llms import AzureOpenAI

st.title('🦜🔗 Digi&Met Test Chatbot')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  OPENAI_API_TYPE = "azure"
  OPENAI_API_VERSION = "2023-05-15"
  OPENAI_API_BASE = "https://azure-openai-resource-lc-001.openai.azure.com/"
  OPENAI_API_KEY = "820bd60818df4af085211b36d91581ea"
  os.environ["OPENAI_API_TYPE"] = OPENAI_API_TYPE
  os.environ["OPENAI_API_VERSION"] = OPENAI_API_VERSION
  os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE
  os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
  load_dotenv()
  DEPLOYMENT_NAME = "ModelDaVinci002LC"
  MODEL_NAME = "text-davinci-002"
  llm = AzureOpenAI(deployment_name=DEPLOYMENT_NAME, model_name=MODEL_NAME, temperature=0.7)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

with st.form('my_form2'):
  text = st.text_area('Enter text:', 'What is the capital of Poland?')
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)

