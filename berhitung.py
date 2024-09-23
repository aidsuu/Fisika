import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.selectbox("Satuan:", ("C", "F", "K", "R"), key='sx')
st.write = ("Anda memamsukkan", x,' ',sx)
sy = st.selectbox("Dikonversi ke:", ("C", "F", "K", "R"), key='sy')
y = 0
if(sx == "C"):
  if(sy == 'C'):
    y = x
  elif(sy == 'F'):
    y = x*9/5+32
  elif(sy == 'K'):
    y = x+2773.15
st.write (x, ' ', sx, ' = ',y, sy)
                 

