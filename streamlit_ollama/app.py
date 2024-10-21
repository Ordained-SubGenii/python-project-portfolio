import streamlit as st
import ollama   

st.title("KbronBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What do you need Kbron?"}]

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="/home/cachegrind/bin/python_projs/avatars/my_avatar.svg").write(msg["content"])
        #st.chat_message(msg["role"], avatar="🧑").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])


## Configure the model
def generate_response():
    response = ollama.chat(model='llama3.2', stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="/home/cachegrind/bin/python_projs/avatars/my_avatar.svg").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar="🤖").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
