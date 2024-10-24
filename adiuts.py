import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Fisika Komputasi Awan')  
st.subheader('Adi Saputra :sparkles:')

# Fungsi untuk menghasilkan titik acak dalam lingkaran yang menyinggung garis x dan y
def generate_random_points_in_circle(num_points, center=(1, 1), radius=1):
    angles = np.random.uniform(0, 2 * np.pi, num_points)  # Sudut acak
    radii = np.sqrt(np.random.uniform(0, 1, num_points)) * radius  # Radius acak
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# Membuat tombol untuk mengubah data acak
if st.button('Data'):
    # Menghasilkan titik acak dalam lingkaran
    num_points = 50
    center = (1, 1)  # Pusat lingkaran
    x, y = generate_random_points_in_circle(num_points, center=center)
    colors = np.random.rand(num_points)
    area = (30 * np.random.rand(num_points))**2  # Ukuran bubble

    # Membuat plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')  # Mengatur aspek ratio menjadi equal
    ax.set_xlim([0, 2.1])  # Batas x pada plot (lingkaran menyinggung sumbu y di 0 dan x di 2)
    ax.set_ylim([0, 2.1])  # Batas y pada plot (lingkaran menyinggung sumbu x di 0 dan y di 2)
    ax.grid(True)  # Mengaktifkan grid

    # Membuat lingkaran batas radius 1, dengan pusat di (1,1)
    circle = plt.Circle(center, 1, color='r', fill=False, linestyle='--')
    ax.add_artist(circle)

    # Plot scatter dan garis ke pusat lingkaran
    for i in range(num_points):
        ax.plot([x[i], center[0]], [y[i], center[1]], color='gray', linestyle='--', linewidth=0.7)  # Garis dari titik ke pusat
        ax.scatter(x[i], y[i], s=area[i], c=np.array([colors[i], colors[i], colors[i]]).reshape(1, -1), alpha=0.5)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Keterangan
st.caption('Titik acak dalam lingkaran yang menyinggung sumbu x dan y, dengan garis menuju pusat lingkaran.')