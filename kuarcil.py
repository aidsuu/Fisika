import streamlit as st
import math

# Title
st.title("Calculation of Regression Parameters")

# Input parameters
n = st.number_input("Enter the value of n (number of data points):", step=1)
sum_x = st.number_input("Enter the sum of x (Σx):")
sum_y = st.number_input("Enter the sum of y (Σy):")
sum_x2 = st.number_input("Enter the sum of x^2 (Σx²):")
sum_xy = st.number_input("Enter the sum of xy (Σxy):")
sum_y2 = st.number_input("Enter the sum of y^2 (Σy²):")

# Calculation of b
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
st.write("b =", b)

# Calculation of a
a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)
st.write("a =", a)

# Calculation of Sy
Sy = math.sqrt(
    (1 / (n - 2)) * (sum_y2 - (sum_x2 * sum_y**2) / (n * sum_x2 - sum_x**2) 
                     - 2 * (sum_x * sum_y * sum_xy) / (n * sum_x2 - sum_x**2) 
                     + (n * sum_xy**2) / (n * sum_x2 - sum_x**2))
)
st.write("Sy =", Sy)

# Calculation of Sb
Sb = Sy * math.sqrt(n / (n * sum_x2 - sum_x**2))
st.write("Sb =", Sb)

# Calculation of Sa
Sa = Sy * math.sqrt(sum_x2 / (n * sum_x2 - sum_x**2))
st.write("Sa =", Sa)

# Calculation of relative errors
Ra = (Sa / a) * 100 if a != 0 else None
Rb = (Sb / b) * 100 if b != 0 else None

st.write("Relative Error of a (Ra) =", Ra, "%")
st.write("Relative Error of b (Rb) =", Rb, "%")
