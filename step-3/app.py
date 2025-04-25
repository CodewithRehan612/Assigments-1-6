import streamlit as st
import random

# Initialize session state variables
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'message' not in st.session_state:
    st.session_state.message = ""

# Set page config
st.set_page_config(
    page_title="Guess the Number Game",
    page_icon="🎮",
    layout="centered"
)

# Title and instructions
st.title("🎮 Guess the Number Game")
st.markdown("""
I'm thinking of a number between 1 and 100. 
You have 10 attempts to guess it!
""")

# Display attempts remaining
st.write(f"Attempts remaining: {10 - st.session_state.attempts}")

# Input for guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Submit button
if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        
        if guess == st.session_state.secret_number:
            st.session_state.message = f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts!"
            st.session_state.game_over = True
        elif guess < st.session_state.secret_number:
            st.session_state.message = "📈 Too low! Try a higher number."
        else:
            st.session_state.message = "📉 Too high! Try a lower number."
            
        if st.session_state.attempts >= 10 and not st.session_state.game_over:
            st.session_state.message = f"Game Over! The number was {st.session_state.secret_number}."
            st.session_state.game_over = True

# Display message
if st.session_state.message:
    st.write(st.session_state.message)

# New game button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.experimental_rerun()

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f0f2f6;
        font-size: 14px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Add footer
st.markdown('<div class="footer">Made by Rehan Aslam</div>', unsafe_allow_html=True)
