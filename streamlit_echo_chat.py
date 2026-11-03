import streamlit as st

st.title("Chat de eco")

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.write(mensaje["content"])

entrada = st.chat_input("Escribí algo...")

if entrada:
    st.session_state.mensajes.append({"role": "user", "content": entrada})
    with st.chat_message("user"):
        st.write(entrada)

    with st.chat_message("assistant"):
        st.write(entrada)
    st.session_state.mensajes.append({"role": "assistant", "content": entrada})
