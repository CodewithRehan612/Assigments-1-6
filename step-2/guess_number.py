import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Guess the Number Game",
    page_icon="🎲",
    layout="centered"
)

# Initialize session state variables if they don't exist
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title and instructions
st.title("🎲 Guess the Number Game!")
st.markdown("""
    I'm thinking of a number between 1 and 100.
    Can you guess it?
""")

# Game logic
if not st.session_state.game_over:
    # Input for user's guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess == st.session_state.number:
            st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
        elif guess < st.session_state.number:
            st.warning("Too low! Try a higher number.")
        else:
            st.warning("Too high! Try a lower number.")
        
        st.info(f"Attempts: {st.session_state.attempts}")

# Reset game button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun()

# Add some styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True) 