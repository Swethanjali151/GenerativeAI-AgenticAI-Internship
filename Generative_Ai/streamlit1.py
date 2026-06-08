import streamlit as st
st.title("hello streamlitter")

st.markdown(
    """ This is a palyground for you to try streamlit and have fun.
    
    *** theres a rainbow [so much] ypu can biuld!

    we prepared a few samples for you get started
    """
)
if st.button("send ballons"):
    st.balloons()