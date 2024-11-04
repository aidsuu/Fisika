import streamlit as st
import math

# Title
st.title("Calculation of Regression Parameters")

# Input parameters with format for precise decimal inputs
n = st.number_input("Enter the value of n (number of data points):", step=1)
sum_x = st.number_input("Enter the sum of x (Σx):", format="%.10f")
sum_y = st.number_input("Enter the sum of y (Σy):", format="%.10f")
sum_x2 = st.number_input("Enter the sum of x^2 (Σx²):", format="%.10f")
sum_xy = st.number_input("Enter the sum of xy (Σxy):", format="%.10f")
sum_y2 = st.number_input("Enter the sum of y^2 (Σy²):", format="%.10f")
sum_x_squared = st.number_input("Enter the square of the sum of x ((Σx)^2):", format="%.10f")

# Denominator check
denominator = n * sum_x2 - sum_x_squared
if denominator == 0:
    st.error("The denominator nΣx² - (Σx)² is zero. Please check your input values.")
else:
    # Calculation of b
    b = (n * sum_xy - sum_x * sum_y) / denominator
    st.write("b =", b)

    # Calculation of a
    a = (sum_y * sum_x2 - sum_x * sum_xy) / denominator
    st.write("a =", a)

    # Calculation of Sy
    Sy_numerator = (sum_y2 - (sum_x2 * sum_y**2) / denominator
                    - 2 * (sum_x * sum_y * sum_xy) / denominator
                    + (n * sum_xy**2) / denominator)
    
    # Check for non-negative Sy_numerator
    if Sy_numerator < 0:
        st.error("Sy numerator is negative, resulting in an invalid square root calculation. Please check your input values.")
    elif n <= 2:
        st.error("The value of n should be greater than 2 for Sy, Sb, and Sa calculations.")
    else:
        Sy = math.sqrt((1 / (n - 2)) * Sy_numerator)
        st.write("Sy =", Sy)

        # Calculation of Sb
        Sb = Sy * math.sqrt(n / denominator)
        st.write("Sb =", Sb)

        # Calculation of Sa
        Sa = Sy * math.sqrt(sum_x2 / denominator)
        st.write("Sa =", Sa)

        # Calculation of relative errors
        Ra = (Sa / a) * 100 if a != 0 else None
        Rb = (Sb / b) * 100 if b != 0 else None

        st.write("Relative Error of a (Ra) =", Ra, "%")
        st.write("Relative Error of b (Rb) =", Rb, "%")
