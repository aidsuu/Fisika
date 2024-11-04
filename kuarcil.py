import streamlit as st
import numpy as np

def calculate_stats(Σxy, Σx, Σy, Σx2, n):
    numerator_b = n * Σxy - Σx * Σy
    denominator_b = n * Σx2 - (Σx)**2
    b = numerator_b / denominator_b

    numerator_a = (Σy * Σx2 - Σx * Σxy)
    denominator_a = n * Σx2 - (Σx)**2
    a = numerator_a / denominator_a

    sy = np.sqrt((1 / (n - 2)) * (Σy**2 - (Σx2 * (Σy)**2 - 2 * Σx * Σy * Σxy + n * (Σxy)**2) / (n * Σx2 - (Σx)**2)))
    sb = sy / np.sqrt(n * Σx2 - (Σx)**2)
    sa = sy * np.sqrt(Σx2 / (n * Σx2 - (Σx)**2))

    r_a = abs(sa / a) * 100
    r_b = abs(sb / b) * 100

    return a, b, sy, sb, sa, r_a, r_b

st.title("Statistical Analysis")

Σxy = st.number_input("Enter Σxy", type=float)
Σx = st.number_input("Enter Σx", type=float)
Σy = st.number_input("Enter Σy", type=float)
Σx2 = st.number_input("Enter Σx^2", type=float)
n = st.number_input("Enter number of data points", type=int)

a, b, sy, sb, sa, r_a, r_b = calculate_stats(Σxy, Σx, Σy, Σx2, n)

st.write(f"Intercept (a): {a:.2f}")
st.write(f"Slope (b): {b:.2f}")
st.write(f"Standard error of y (sy): {sy:.2f}")
st.write(f"Standard error of b (sb): {sb:.2f}")
st.write(f"Standard error of a (sa): {sa:.2f}")
st.write(f"Relative Precision of a: {r_a:.2f}%")
st.write(f"Relative Precision of b: {r_b:.2f}%")
