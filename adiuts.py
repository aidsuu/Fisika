import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Fisika Komputasi Awan')  
st.subheader('Adi Saputra :sparkles:')

# Membuat tombol untuk mengubah data acak
if st.button('Data'):
    # Membuat data acak
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    area = (30 * np.random.rand(50))**2  # Ukuran bubble

    # Membuat plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(x, y, s=area, c=colors, alpha=0.5)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Keterangan
st.caption('Data acak yang berubah setiap tombol ditekan')
