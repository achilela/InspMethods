# app.py
import os
import asyncio
from dotenv import load_dotenv
import streamlit as st

async def main():
    load_dotenv()
    st.title("🚀 Twin - Methods Engineer with RAG 🚀")

    chat_interface = EnhancedChatInterface(
        api_key=os.getenv("NVIDIA_API_KEY"),
        base_url="https://integrate.api.nvidia.com/v1"
    )

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf"])
        if uploaded_file:
            content = process_file(uploaded_file)
            chat_interface.initialize_rag(content)
            st.success("Document processed")

        if st.button("Save Chat"):
            filename = chat_interface.save_chat_history()
            st.success(f"Chat saved to {filename}")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            await chat_interface.get_ai_response(st.empty(), prompt)

if __name__ == "__main__":
    asyncio.run(main())
