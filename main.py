import streamlit as st
#from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain_openai.chat_models import ChatOpenAI

# Load environment variables
#load_dotenv()

# Initialize LangChain and ChatOpenAI
llm = OpenAI()
chat_model = ChatOpenAI()

content = "ESG 공급망"
content2 = "한국"
title = st.text_input("문의 사항을 입력해주세요!")

# st.button("Reset", type="primary")
if st.button("검색하기"):
    with st.spinner("Searching..."):
        # Combine input content
        combined_content = content + content2 + title

        # Invoke with LangChain
        result = llm.invoke(combined_content)

        # Invoke with ChatOpenAI
        result2 = chat_model.invoke(combined_content)

        # Create a Markdown representation of the conversation
        # conversation = f"**User Input:**\n{combined_content}\n\n**LangChain Result:**\n{result}\n\n**ChatOpenAI Result:**\n{result2}"

        # Print the conversation
        st.title("공급망AS")

        st.write("인공지능 답변입니다. ", result)
        st.write("채팅 답변입니다. ", result2)
else:
    st.write("취소")
