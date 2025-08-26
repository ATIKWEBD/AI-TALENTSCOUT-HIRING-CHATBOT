# app.py

import streamlit as st
import google.generativeai as genai
import os



api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure.api_key = api_key
else:
    st.error("Google API key not found. Please add it to your .env file.")
    st.stop()

# Setting  the title for the Streamlit app
st.title("TalentScout Hiring Assistant 🤖")

# System prompt to define the chatbot's role and instructions
SYSTEM_PROMPT = """
You are an intelligent and friendly hiring assistant chatbot for 'TalentScout,' a tech recruitment agency. Your purpose is to conduct an initial screening of candidates.
Your tasks are:
1. Greet the candidate warmly and explain your purpose.
2. Gather essential information in this specific order: Full Name, Email Address, Phone Number, Years of Experience, Desired Position(s), Current Location, and Tech Stack (programming languages, frameworks, databases, tools). Ask for only one piece of information at a time.
3. After gathering all the information, generate exactly 3-5 relevant technical questions based on the candidate's declared tech stack.
4. Once you have asked the questions, do not evaluate the answers. Conclude the conversation gracefully, thanking the candidate and telling them a recruiter will be in touch.
5. If the user asks something unrelated to the screening process, politely steer the conversation back to the task at hand. You must not deviate from your purpose.
6. If the user says "goodbye", "exit", or a similar keyword, end the conversation.
"""

# Initializing chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    # Add the initial greeting from the assistant
    st.session_state.messages.append(
        {"role": "assistant", "content": "Hello! I'm the AI Hiring Assistant for TalentScout. I'll be asking a few questions to get started with your screening process. What is your full name?"}
    )

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] != "system": # Don't display the system prompt
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Your response..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # The key to context is sending the entire chat history
        import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.5-flash")


role_map = {"user": "user", "assistant": "model"}

history = [
    {"role": role_map.get(m["role"], "user"), "parts": [m["content"]]}
    for m in st.session_state.messages
]

# Streaming response
response_stream = model.generate_content(
    history,
    stream=True
)
full_response = ""  
with st.chat_message(""):
        placeholder = st.empty()
        for chunk in response_stream:
            if not chunk.candidates:
                continue
            part = chunk.candidates[0].content.parts[0] if chunk.candidates[0].content.parts else None
            if part and part.text:
                full_response += part.text
                placeholder.markdown(full_response + "▌") 
        placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})