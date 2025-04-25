import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)"""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return BMI category based on BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Set page config
st.set_page_config(
    page_title="BMI Calculator📲",
    page_icon="⚖️",
    layout="centered"
)

# Add title and description
st.title("BMI Calculator")
st.markdown("""
This app calculates your Body Mass Index (BMI) based on your height and weight.
""")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    # Weight input
    weight = st.number_input(
        "Enter your weight (kg)",
        min_value=20.0,
        max_value=300.0,
        value=70.0,
        step=0.1
    )

with col2:
    # Height input
    height = st.number_input(
        "Enter your height (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.70,
        step=0.01
    )

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    # Display results
    st.markdown("---")
    st.subheader("Your BMI Results")
    st.metric("BMI", f"{bmi:.1f}")
    st.info(f"Category: {category}")
    
    # Add BMI scale visualization
    st.markdown("---")
    st.subheader("BMI Scale")
    st.progress(min(1.0, bmi/40))  # Scale progress bar to max 40 BMI
    
    # Add BMI category explanation
    st.markdown("""
    **BMI Categories:**
    - Underweight: < 18.5
    - Normal weight: 18.5 - 24.9
    - Overweight: 25 - 29.9
    - Obese: ≥ 30
    """)

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ by Rehan Aslam using Streamlit")
