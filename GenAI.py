import streamlit as st
from google import genai
robo = genai.Client(api_key="")
mychat = robo.chats.create(model="gemini-flash-lite-latest")
st.title("My Ai")

question = st.text_input("Aks any")
if st.button("Send"):
  response = mychat.send_message(question)
  st.write(response.text)
