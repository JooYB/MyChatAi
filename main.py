import streamlit as st

#from langchain_core.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
#from dotenv import load_dotenv
#load_dotenv()

# Initialize LangChain and ChatOpenAI

chat_model = ChatOpenAI()

content1 = "ESG"
content2 = "한국"
title = st.text_input("문의 사항을 입력해주세요!")

# st.button("Reset", type="primary")
if st.button("검색하기"):
    with st.spinner("Searching..."):
        # Combine input content
        combined_content = content1 + content2 + title

        #result = chat_model.invoke(combined_content)
        result = chat_model.predict(combined_content)

        st.title("공급망 https://www.esgsupport.or.kr")
        
        #st.write("인공지능 답변입니다. ", result)
        #st.write("채팅 답변입니다. ", html_content)
        st.markdown(result, unsafe_allow_html=True)
else:
    st.write("취소")
