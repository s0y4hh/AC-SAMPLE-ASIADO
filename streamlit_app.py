import streamlit as st

import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

# Streamlit app layout
st.title("Simple Calculator")

# User input for numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# User input for operation
operation = st.selectbox("Select an operation:", ['Add', 'Subtract', 'Multiply', 'Divide'])

# Calculate button
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"The result is: {result}")

# Footer
st.write("Made with ❤️ using Streamlit")
