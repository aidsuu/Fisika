import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write("Anda memasukka", x, ' ', sx)
sy = st.text_input("Dikonversi ke", "F")
y = 0
if(sx == "C"):
  if(sy == 'C'):
    y = x
  elif(sy == 'F'):
    y = x*9/5+32
st.write (x, ' ', sx, ' = ',y, sy)

with st.popover("Konversi Suhu"):
    st.markdown("Konversi Suhu 👋")
    name = st.text_input("Ingin Konversi apa?")

st.write("Your name:", name)
