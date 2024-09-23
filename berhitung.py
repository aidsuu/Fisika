import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.selectbox("Satuan", ("C", "F", "R", "K"), key='sx')
st.write ("Anda memasukkan", x,'',sx)
sy = st.selectbox("Dikonversi ke", ("C", "F", "R", "K"), key='sy')

y = 0

if sx == 'C':  # Celsius
    if sy == 'C':
        y = x
    elif sy == 'F':  
        y = (9/5) * x + 32
    elif sy == 'K':  
        y = x + 273
    elif sy == 'R': 
        y = x * 4/5
elif sx == 'F':  
    if sy == 'C':  
        y = (x - 32) * 5/9
    elif sy == 'F':
        y = x
    elif sy == 'K': 
        y = (x - 32) * 5/9 + 273
    elif sy == 'R':  
        y = (x - 32) * 4/9
elif sx == 'K':  
    if sy == 'C':  
        y = x - 273
    elif sy == 'F':  
        y = (x - 273) * 9/5 + 32
    elif sy == 'K':
        y = x
    elif sy == 'R':  
        y = (x - 273) * 0.8
elif sx == 'R':  # Reaumur
    if sy == 'C':  
        y = x / 0.8
    elif sy == 'F':  
        y = (x * 9/4) + 32
    elif sy == 'K': 
        y = (x / 0.8) + 273
    elif sy == 'R':
        y = x

st.write(x, sx, "=", y, sy)
