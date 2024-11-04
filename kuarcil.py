import streamlit as st
import math

# Title
st.title("Calculation of Regression Parameters")

# Input parameters with precise formatting and small step size for exact decimal values
n = st.number_input("Enter the value of n (number of data points):", step=1)
sum_x = st.number_input("Enter the sum of x (Σx):", format="%.10f", step=0.0000000001)
sum_y = st.number_input("Enter the sum of y (Σy):", format="%.10f", step=0.0000000001)
sum_x2 = st.number_input("Enter the sum of x^2 (Σx²):", format="%.10f", step=0.0000000001)
sum_xy = st.number_input("Enter the sum of xy (Σxy):", format="%.10f", step=0.0000000001)
sum_y2 = st.number_input("Enter the sum of y^2 (Σy²):", format="%.10f", step=0.0000000001)
sum_x_squared = st.number_input("Enter the square of the sum of x ((Σx)^2):", format="%.10f", step=0.0000000001)
sum_y_squared = st.number_input("Enter the square of the sum of y ((Σy)^2):", format="%.10f", step=0.0000000001)

# Step 1: Check denominator to prevent division by zero
denominator = n * sum_x2 - sum_x_squared
if denominator == 0:
    st.error("The denominator nΣx² - (Σx)² is zero. Please check your input values.")
else:
    # Calculation of b
    b = (n * sum_xy - sum_x * sum_y) / denominator
    st.write("Calculated value of b:", b)

    # Calculation of a
    a = (sum_y * sum_x2 - sum_x * sum_xy) / denominator
    st.write("Calculated value of a:", a)

    # Calculation of Sy (Standard deviation of y)
    Sy_numerator = (
        sum_y2
        - (sum_x2 * sum_y_squared - 2 * sum_x * sum_y * sum_xy + n * sum_xy**2) / denominator
    )
    if Sy_numerator < 0:
        st.error("Sy numerator is negative, resulting in an invalid square root calculation. Please check your input values.")
    elif n <= 2:
        st.error("The value of n should be greater than 2 for Sy, Sb, and Sa calculations.")
    else:
        Sy = math.sqrt(Sy_numerator / (n - 2))
        st.write("Calculated value of Sy:", Sy)

        # Calculation of Sb (Standard error of b)
        Sb = Sy * math.sqrt(n / denominator)
        st.write("Calculated value of Sb:", Sb)

        # Calculation of Sa (Standard error of a)
        Sa = Sy * math.sqrt(sum_x2 / denominator)
        st.write("Calculated value of Sa:", Sa)

        # Calculation of relative errors for a and b
        Ra = (Sa / abs(a)) * 100 if a != 0 else None
        Rb = (Sb / abs(b)) * 100 if b != 0 else None

        # Displaying the relative errors
        st.write("Relative Error of a (Ra):", Ra, "%")
        st.write("Relative Error of b (Rb):", Rb, "%")
