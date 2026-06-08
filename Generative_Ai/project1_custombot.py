import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
os.environ["GOOGLE_API_KEY"]="ENTER UR GEMINI API KEY HERE"
os.environ["LANGSMITH_TRACING_V2"]="true"

os.environ["LANGSMITH_API_KEY"]="ENTER UR LANGSMITH API KEY HERE"
# prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a chat bot which assisatnace to the world and about the latest news"),
        ("human","{question}")
    ]
)

st.title("Gemini chat model created by Swethanjali")
input_text=st.text_input("How may I help you Today? Swetha....")


llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7,max_output_tokens=2000)
output_parser=StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
    with st.spinner("Generative response..."):
        try:
            response=chain.invoke({'question':input_text})
            st.success("response generated successs")
            st.write(response)
        except Exception as e:
            st.error(f'An error occoured:{e}')
