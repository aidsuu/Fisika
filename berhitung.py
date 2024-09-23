import streamlit as st

x = st.number_input(
  "Insert a number", value=none, placeholder="Type a number..."
)
st.writer("The current number is ", x)
st.later(r'''
x^2 =
''')
st.write(x*x)
