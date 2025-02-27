import streamlit as st
import numpy as np
import time

# Function to perform unit conversion
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ('meters', 'kilometers'): 0.001,
        ('kilometers', 'meters'): 1000,
        ('grams', 'kilograms'): 0.001,
        ('kilograms', 'grams'): 1000,
        ('celsius', 'fahrenheit'): lambda c: (c * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9,
        ('liters', 'milliliters'): 1000,
        ('milliliters', 'liters'): 0.001,
        ('miles', 'kilometers'): 1.60934,
        ('kilometers', 'miles'): 0.621371,
    }
    
    if (from_unit, to_unit) in conversion_factors:
        factor = conversion_factors[(from_unit, to_unit)]
        if callable(factor):
            return factor(value)
        else:
            return value * factor
    else:
        return None

# Streamlit app
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Advanced Unit Converter")
st.markdown("### Convert between different units with style! 🌟")

# Sidebar for unit selection
st.sidebar.header("Select Units")

# Define valid unit pairs
valid_units = {
    'Length': ['meters', 'kilometers', 'miles'],
    'Weight': ['grams', 'kilograms'],
    'Temperature': ['celsius', 'fahrenheit'],
    'Volume': ['liters', 'milliliters']
}

# Select category
category = st.sidebar.selectbox("Category", list(valid_units.keys()))

# Select units based on category
from_unit = st.sidebar.selectbox("From Unit", valid_units[category])
to_unit = st.sidebar.selectbox("To Unit", valid_units[category])

# Input value
value = st.number_input("Enter the value to convert", min_value=0.0, step=0.1)

# Convert button
if st.button("Convert"):
    with st.spinner('Converting...'):
        time.sleep(1)  # Simulate a delay for animation
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.success(f"**{value} {from_unit}** is equal to **{result:.2f} {to_unit}** 🎉")
            if from_unit in ['celsius', 'fahrenheit']:
                formula = f"({value}° {from_unit[0].upper()}) to {to_unit[0].upper()}"
            else:
                formula = f"{value} {from_unit} * conversion factor = {result:.2f} {to_unit}"
            st.markdown(f"**Formula used:** {formula}")
            st.snow()  # Add snow animation
        else:
            st.error("Conversion not supported. 😞")

# Add some animation
st.balloons()

# Feedback section
st.markdown("### We value your feedback! 💬")
feedback = st.text_area("Please leave your feedback here:")

# Custom styled button
button_style = """
    <style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback! 🙌")
    else:
        st.warning("Please enter some feedback before submitting. ⚠️")
