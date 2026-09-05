import streamlit as st

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Smart Calculator")
st.write("A simple calculator built using Python and Streamlit.")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Choose an operation",
    ["Addition ➕", "Subtraction ➖", "Multiplication ✖️",
     "Division ➗", "Percentage %", "Power 🔢"]
)

if st.button("Calculate 🚀"):
    if operation == "Addition ➕":
        result = num1 + num2

    elif operation == "Subtraction ➖":
        result = num1 - num2

    elif operation == "Multiplication ✖️":
        result = num1 * num2

    elif operation == "Division ➗":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            st.stop()
        result = num1 / num2

    elif operation == "Percentage %":
        result = (num1 / 100) * num2

    elif operation == "Power 🔢":
        result = num1 ** num2

    st.success(f"🎯 Result: {result}")
