import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Guess the Number Game",
    page_icon="🎲",
    layout="centered"
)

# Initialize session state variables
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title and description
st.title("🎲 Guess the Number Game")
st.markdown("""
    Welcome to the Guess the Number game! 
    I'm thinking of a number between 1 and 100. 
    Can you guess what it is?
""")

# Game logic
if not st.session_state.game_over:
    # Input for user's guess
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, value=1)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        # Provide feedback
        if user_guess < st.session_state.target_number:
            st.warning("Too low! Try a higher number.")
        elif user_guess > st.session_state.target_number:
            st.warning("Too high! Try a lower number.")
        else:
            st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
    
    # Display attempts
    st.info(f"Number of attempts: {st.session_state.attempts}")
    
    # Add a hint button
    if st.button("Get a Hint"):
        if user_guess < st.session_state.target_number:
            st.info(f"The number is between {user_guess} and 100")
        else:
            st.info(f"The number is between 1 and {user_guess}")

# Reset game button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.target_number = random.randint(1, 100)
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