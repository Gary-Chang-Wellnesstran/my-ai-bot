import streamlit as st
import google.generativeai as genai
import os

# 1. 介面設定
st.title("我的 AI 助手")
st.caption("基於 Gemini 1.5 Flash 建立")

# 2. 從系統安全獲取 API Key (這步很重要，等等會教怎麼設定)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 建立對話紀錄（讓網頁重新整理時不會消失）
if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示過去的對話
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. 接收使用者輸入
if prompt := st.chat_input("想問什麼？"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. 呼叫 Gemini 產生回應
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})