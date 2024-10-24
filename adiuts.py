import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Fisika Komputasi Awan')  
st.subheader('Adi Saputra :sparkles:')

# Fungsi untuk menghasilkan titik acak dalam lingkaran
def generate_random_points_in_circle(num_points, radius=0.5):  # radius 0.5 karena skala -0.5 ke 0.5
    angles = np.random.uniform(0, 2 * np.pi, num_points)  # Sudut acak
    radii = np.sqrt(np.random.uniform(0, 1, num_points)) * radius  # Radius acak
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y

# Membuat tombol untuk mengubah data acak
if st.button('Data'):
    # Menghasilkan titik acak dalam lingkaran
    num_points = 100
    x, y = generate_random_points_in_circle(num_points)
    colors = np.random.rand(num_points, 3)  # RGB colors
    area = (30 * np.random.rand(num_points))**2  # Ukuran bubble

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim([-0.75, 0.75])  # Batas plot diperkecil untuk fokus pada area data
    ax.set_ylim([-0.75, 0.75])
    ax.grid(True)
    
    # Membuat garis sumbu x dan y
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

    # Membuat lingkaran batas radius 0.5 di pusat (0,0)
    circle = plt.Circle((0, 0), 0.5, color='r', fill=False, linestyle='--')
    ax.add_artist(circle)

    # Plot scatter dan garis ke pusat lingkaran
    for i in range(num_points):
        ax.plot([x[i], 0], [y[i], 0], color='gray', linestyle='--', linewidth=0.5, alpha=0.3)  # Garis ke pusat
        ax.scatter(x[i], y[i], s=area[i], c=[colors[i]], alpha=0.5)

    # Menambahkan titik pusat
    ax.scatter(0, 0, color='green', s=50, zorder=5)

    # Mengatur label sumbu
    ax.set_xticks(np.arange(-0.75, 1, 0.25))
    ax.set_yticks(np.arange(-0.75, 1, 0.25))

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Keterangan
st.caption('Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 0.5')