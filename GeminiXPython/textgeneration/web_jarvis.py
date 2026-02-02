
# Here, this is the visual representation in stremlit of the chatbot
# In order to run this :
# firstly pip install streamlit 
# and then in the terminal after writing the code
# streamlit run textgeneration/web_jarvis.py


import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()    # Python searches and loads api key from .env file in the system

st.set_page_config(page_title="Jarvis AI", page_icon="🤖")
st.title("🤖 Jarvis Web Assistant")

# 1. ALWAYS create a fresh client on every rerun
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Store ONLY the history (text), not the "Chat Object"
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle input
if prompt := st.chat_input("Ask Jarvis..."):
    # Add user message to UI and history
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 5. REBUILD THE CHAT with history on every click
    # This prevents the "Client Closed" error entirely
    formatted_history = [
        # Crucial Fix: Gemini requires 'model', but Streamlit likes 'assistant'
        {"role": "model" if m["role"] == "assistant" else "user", 
         "parts": [{"text": m["content"]}]} 
        for m in st.session_state.messages[:-1] # Don't include the current prompt yet
    ]
    
    chat = client.chats.create(model="gemini-2.0-flash", history=formatted_history)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        
        try:
            # Send the prompt to the rebuilt session
            for chunk in chat.send_message_stream(prompt):
                full_response += chunk.text
                placeholder.markdown(full_response + "▌")
            
            placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Jarvis Error: {e}")