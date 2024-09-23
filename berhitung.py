import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write("Anda memasukka", x, ' ', sx)
sy = st.text_input("Dikonversi ke", "F")
sz = st.text_input("Dikonversi ke", "K")
y = 0
if(sx == "C"):
  if(sy == 'C'):
    y = x
  elif(sy == 'F'):
    y = x*9/5+32

z = 0
if(sx == "C"):
  elif(sz == "C"):
    z = x
  elif(sz == 'K'):
    z = x+273.15
st.write (x, ' ', sx, ' = ',y, sy)
st.write (x, ' ', sx, ' = ',z, sz)
