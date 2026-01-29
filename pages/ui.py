import streamlit as st 
import os , pandas as pd
import sys , time
import plotly.express as fancyplot
import api , caption_prompt , query_prompt
import time
import sqlite3

dbs = os.getcwd()+"/data.sqlite3"

cursor = sqlite3.connect(dbs)


intial_caption = """
### Hi there , Welcome to movielyze , talk to the dataset , however you like!!
### Example Queries
- ### Top 10 Movies
- ### Director of the most acclaimed drama movie"""

st.markdown(intial_caption)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant","content":0,"caption":"Start with examples above!!"}]


st.chat_input(placeholder="""Talk to the Dataset!!\nEx: Top 10 Movies""",key="chatput")
prompt_input = st.session_state.get("chatput")
if prompt_input != None:
    try:
        st.session_state.messages.append({"role":"user","content":prompt_input})
        data = api.post_ai(query_prompt.query_prompt,prompt_input)
        datas = cursor.execute(data)
        givedata  = datas.fetchall()
        caption_data = api.post_ai(caption_prompt.prompt,prompt_input)
        st.session_state.messages.append({"role":"assistant","content":givedata,"caption":caption_data})
    except (Exception,sqlite3.Error,sqlite3.OperationalError) as ie:
        st.session_state.messages.append({"role":"system","content":f"{ie} occured"})
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"],avatar=os.getcwd()+"/user.png").write(msg["content"])
    elif msg["role"] == "assistant":
        assistant_response = st.chat_message(msg["role"],avatar=os.getcwd()+"/the.webp")
        assistant_response.write(msg["caption"])
        if msg["content"] != 0:
            assistant_response.dataframe(msg["content"])