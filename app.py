# app.py
import streamlit as st
from late_fee import calculate_late_fee   # reuses your existing function

st.title("Library Late Fee Calculator")

days_late = st.number_input("How many days late?", min_value=0, value=0, step=1)
fee = calculate_late_fee(days_late)

st.write(f"### Late fee: Rs. {fee}")
if fee == 500:
    st.warning("Maximum fee reached (capped at Rs. 500)")
