import streamlit as st
import numpy as np

st.title("Kalkulator Koefisien Korelasi")

st.write("Masukkan data x dan y:")
x_data = st.text_input("Data x (pisahkan dengan koma)", "1,2,3,4,5")
y_data = st.text_input("Data y (pisahkan dengan koma)", "2,4,6,8,10")

# Proses data
x = np.fromstring(x_data, dtype=float, sep=",")
y = np.fromstring(y_data, dtype=float, sep=",")

# Hitung nilai-nilai yang dibutuhkan
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x ** 2)
sum_y2 = np.sum(y ** 2)

# Hitung koefisien korelasi
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x ** 2)
sy = np.sqrt((1 / (n - 2)) * (sum_y2 - (sum_x2 * sum_y2) / n - 2 * (sum_x * sum_y * sum_xy) / n + (n * sum_xy ** 2) / n))
sb = sy * np.sqrt(n / (n * sum_x2 - sum_x ** 2))
sa = sy * np.sqrt(sum_x2 / (n * sum_x2 - sum_x ** 2))

# Tampilkan hasil
st.write("Koefisien Korelasi (b):", b)
st.write("Koefisien Korelasi (a):", a)
st.write("Standar Deviasi Y:", sy)
st.write("Standar Deviasi b:", sb)
st.write("Standar Deviasi a:", sa)
st.write("Ralat Relatif
