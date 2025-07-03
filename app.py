import streamlit as st
st.image("039.jpg")
st.title("Dell Global Business Center Sdn. Bhd.")

st.date_input("Transaction Date")
st.radio("Your Department:", ["NPI", "QA", "Test", "Operation"])
st.camera_input("Case Reported:")