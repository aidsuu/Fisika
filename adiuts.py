import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Fisika Komputasi Awan')  
st.subheader('Adi Saputra :sparkles:')

# Fungsi untuk menghasilkan titik acak dalam lingkaran radius 1
def generate_random_points_in_circle(num_points):
    angles = np.random.uniform(0, 2 * np.pi, num_points)  # Sudut acak
    radii = np.sqrt(np.random.uniform(0, 1, num_points))  # Radius acak dengan sqrt untuk distribusi merata
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y

# Membuat tombol untuk mengubah data acak
if st.button('Data'):
    # Menghasilkan titik acak dalam lingkaran
    num_points = 50
    x, y = generate_random_points_in_circle(num_points)
    colors = np.random.rand(num_points)
    area = (30 * np.random.rand(num_points))**2  # Ukuran bubble

    # Membuat plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')  # Mengatur aspek ratio menjadi equal
    ax.set_xlim([-1.1, 1.1])  # Batas x pada plot
    ax.set_ylim([-1.1, 1.1])  # Batas y pada plot
    scatter = ax.scatter(x, y, s=area, c=colors, alpha=0.5)

    # Membuat lingkaran batas radius 1
    circle = plt.Circle((0, 0), 1, color='r', fill=False, linestyle='--')
    ax.add_artist(circle)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Keterangan
st.caption('Titik acak dalam lingkaran radius 1 yang berubah setiap tombol ditekan')