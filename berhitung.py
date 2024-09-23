import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write("Anda memasukka", x, ' ', sx)
sy = st.text_input("Dikonversi ke", "F")

st.write (x, ' ', sx, '=...', sy)
