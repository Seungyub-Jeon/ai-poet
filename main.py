# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('시 작성기')

content = st.text_input('시의 주제를 제시해 주세요')
if st.button('시 작성하기'):
    with st.spinner('Wait for it...'):
        result = chat_model.predict(content+ "에 대하여 시를 작성해줘") 
        st.write(result)

