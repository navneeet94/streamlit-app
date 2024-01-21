import streamlit as st

st.title("Movies List")
arr = ['Amazing Spider Man', 'Avengers', 'Hanna Montana']
option = st.selectbox(
    'Select Your Movie',arr)
