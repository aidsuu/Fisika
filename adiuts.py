import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Fisika Komputasi Awan')  
st.subheader('Adi Saputra :sparkles:')

# Fungsi untuk menghasilkan titik acak dalam lingkaran
def generate_random_points_in_circle(num_points, radius=1):
    angles = np.random.uniform(0, 2 * np.pi, num_points)  # Sudut acak
    radii = np.sqrt(np.random.uniform(0, 1, num_points)) * radius  # Radius acak
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y

# Membuat tombol untuk mengubah data acak
if st.button('Data'):
    # Menghasilkan titik acak dalam lingkaran
    num_points = 100  # Meningkatkan jumlah titik untuk visualisasi yang lebih baik
    x, y = generate_random_points_in_circle(num_points)
    colors = np.random.rand(num_points, 3)  # RGB colors
    area = (30 * np.random.rand(num_points))**2  # Ukuran bubble

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim([-1.1, 1.1])  # Sedikit lebih besar dari radius untuk margin
    ax.set_ylim([-1.1, 1.1])
    ax.grid(True)

    # Membuat lingkaran batas radius 1 di pusat (0,0)
    circle = plt.Circle((0, 0), 1, color='r', fill=False, linestyle='--')
    ax.add_artist(circle)

    # Plot scatter dan garis ke pusat lingkaran
    for i in range(num_points):
        ax.plot([x[i], 0], [y[i], 0], color='gray', linestyle='--', linewidth=0.5, alpha=0.3)  # Garis ke pusat
        ax.scatter(x[i], y[i], s=area[i], c=[colors[i]], alpha=0.5)

    # Menambahkan titik pusat
    ax.scatter(0, 0, color='green', s=50, zorder=5)  # Titik pusat dengan warna hijau

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Keterangan
st.caption('Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1')