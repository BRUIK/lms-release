import late_fee
import streamlit as st

# Page Title
st.title("Library Late Fee Calculator")

# Number Input Field
days_late = st.number_input(
    "How many days late?", min_value=0, value=0, step=1
)

# Calculate fee using the function from late_fee.py
fee = late_fee.calculate_late_fee(days_late)

# Display Result
st.header(f"Late fee: Rs. {fee}")