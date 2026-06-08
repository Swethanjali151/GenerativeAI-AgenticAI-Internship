import streamlit as st
st.title("Internship batch")
st.write("Basic Ui code")
st.header("select a number")
number=st.slider("select a number",0,50,5)
st.subheader("result:")
square=number**2
st.write(f"square of{number} is {square}")