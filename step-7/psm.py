import streamlit as st
import re

def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Add more characters.")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
    
    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers for stronger password.")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")
    
    # Check for common patterns
    if re.search(r"(.)\1\1", password):  # Check for repeated characters
        score -= 1
        feedback.append("Avoid repeated characters.")
    
    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"
    
    return strength, feedback, color


# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("🔍 Check how strong your password is!")

# Password input
password = st.text_input("🔑 Enter your password:", type="password")

if password:
    strength, feedback, color = check_password_strength(password)
    
    # Display strength with colored box
    st.markdown(f"""
        <div style="padding: 10px; 
                    border-radius: 5px; 
                    background-color: {color}; 
                    color: white; 
                    text-align: center;">
        🏋️ Password Strength: {strength}
        </div>
    """, unsafe_allow_html=True)
    
    # Display feedback if any
    if feedback:
        st.write("### 💡 Suggestions to improve your password:")
        for suggestion in feedback:
            st.write(f"✨ {suggestion}")
            
    # Display password criteria
    st.write("### ✅ Password Criteria:")
    st.write("📏 Minimum 8 characters (12+ recommended)")
    st.write("🔢 Include numbers")
    st.write("📝 Include lowercase letters")
    st.write("📈 Include uppercase letters")
    st.write("⚡ Include special characters")
    st.write("⚠️ Avoid repeated characters")

