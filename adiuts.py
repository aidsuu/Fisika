import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Fisika Komputasi Awan')  
st.subheader('Adi Saputra :sparkles:')

# Fungsi untuk menghasilkan titik acak dalam lingkaran
def generate_random_points_in_circle(num_points):
    angles = np.random.uniform(0, 2 * np.pi, num_points)
    radii = np.sqrt(np.random.uniform(0, 1, num_points))
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y

# Membuat tombol untuk mengubah data acak
if st.button('Data'):
    # Menghasilkan titik acak dalam lingkaran
    num_points = 100
    x, y = generate_random_points_in_circle(num_points)
    
    # Membuat warna pastel acak
    colors = np.random.uniform(0.5, 1, (num_points, 3))  # Menggunakan nilai minimum 0.5 untuk warna pastel
    area = (50 * np.random.rand(num_points))**2  # Ukuran bubble yang lebih bervariasi

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Set aspek rasio dan batasan plot
    ax.set_aspect('equal')
    ax.set_xlim([-1.00, 1.00])
    ax.set_ylim([-1.00, 1.00])
    
    # Mengatur grid dan ticks
    ax.grid(True, linestyle='-', alpha=0.2)
    ticks = np.arange(-1.00, 1.25, 0.25)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    
    # Format tick labels dengan 2 desimal
    ax.set_xticklabels([f'{x:.2f}' for x in ticks])
    ax.set_yticklabels([f'{y:.2f}' for y in ticks])
    
    # Menambahkan label sumbu
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Membuat lingkaran batas radius 1 di pusat (0,0)
    circle = plt.Circle((0, 0), 1, color='red', fill=False, linestyle='--', alpha=0.5)
    ax.add_artist(circle)

    # Plot scatter dan garis ke pusat lingkaran
    for i in range(num_points):
        ax.plot([x[i], 0], [y[i], 0], color='gray', linestyle='--', linewidth=0.5, alpha=0.2)
        ax.scatter(x[i], y[i], s=area[i], c=[colors[i]], alpha=0.5)

    # Menambahkan titik pusat dengan warna hijau yang lebih kecil
    ax.scatter(0, 0, color='green', s=30, zorder=5)
    
    # Menambahkan judul plot
    plt.title('Data Acak yang berubah setiap tombol ditekan', pad=10, fontsize=10)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# Keterangan
st.caption('Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1')