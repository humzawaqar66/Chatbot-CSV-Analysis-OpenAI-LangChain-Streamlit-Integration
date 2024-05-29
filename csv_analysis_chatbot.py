import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI
from apikey import apikey

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = apikey

# Define Streamlit app
def app():
      # Title and description
    st.title("CSV Query App")
    st.write("Upload a CSV file and enter a query to get an answer.")
    file =  st.file_uploader("Upload CSV file",type=["csv"])
    if not file:
        st.stop()

    data = pd.read_csv(file)
    st.write("Data Preview:")
    st.dataframe(data) 

    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0,model="gpt-4-turbo"),
        data,
        verbose=True,
        agent_executor_kwargs={"handle_parsing_errors": True}
        ) 
    query = st.text_input("Chat with your csv_file: ") 
    messages = [
    ("system", "You are an expert Data Analyst. You can do analysis on provided Dataframe. You give constuctive analaysis as response to user queries"),
    ("human", query)
    ]


    
    if st.button("Send"):

        answer = agent.invoke(messages)
        st.write("Response:")
        st.write(answer['output'])

        #st.bar_chart(data, x= query, y=["output"],use_container_width=True)
        #st.bar_chart(data, x= "isAlive", y=[query],use_container_width=True)

        #st.line_chart(data, y=[query])

if __name__ == "__main__":
    app()   