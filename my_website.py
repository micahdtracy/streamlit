import pandas as pd
import streamlit as st
import numpy as np
from google import genai
import os

st.image("./sunset_pic.jpg")
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
chat = client.chats.create(model="gemini-2.5-flash")



st.title("Micah's ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

  
    # response = f"Echo: {prompt}"
    res = chat.send_message(prompt)
    # print(res.text)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(res.text)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": res.text})
   

# Chat

# while True:
#     message = input("> ")
#     if message == "exit":
#         break

#     res = chat.send_message(message)
#     print(res.text)
# st.write("Hello Zack!!!")