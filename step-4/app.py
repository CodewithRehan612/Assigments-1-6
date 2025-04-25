import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Rock, Paper, Scissors Game - By Rehan Aslam",
    page_icon="🎮",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        height: 3em;
        margin: 0.5em 0;
        font-size: 1.2em;
    }
    .result-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }
    .author-credit {
        background-color: #f0f2f6;
        padding: 0.5rem;
        border-radius: 5px;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎮 Rock, Paper, Scissors Game")
st.markdown('<div class="author-credit">Created by Rehan Aslam</div>', unsafe_allow_html=True)
st.markdown("Choose your move and play against the computer!")

# Initialize session state for score tracking
if 'score' not in st.session_state:
    st.session_state.score = {'player': 0, 'computer': 0}

# Game logic
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        st.session_state.score['player'] += 1
        return "You win! 🎉"
    else:
        st.session_state.score['computer'] += 1
        return "Computer wins! 😢"

# Create columns for the game interface
col1, col2, col3 = st.columns(3)

# Player choice buttons
with col1:
    if st.button("🪨 Rock"):
        player_choice = 'rock'
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        st.session_state.last_game = {
            'player': player_choice,
            'computer': computer_choice,
            'result': result
        }

with col2:
    if st.button("📄 Paper"):
        player_choice = 'paper'
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        st.session_state.last_game = {
            'player': player_choice,
            'computer': computer_choice,
            'result': result
        }

with col3:
    if st.button("✂️ Scissors"):
        player_choice = 'scissors'
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        st.session_state.last_game = {
            'player': player_choice,
            'computer': computer_choice,
            'result': result
        }

# Display game results if a game has been played
if 'last_game' in st.session_state:
    st.markdown("---")
    st.markdown("### Game Results")
    
    # Create columns for the score display
    score_col1, score_col2 = st.columns(2)
    
    with score_col1:
        st.metric("Your Score", st.session_state.score['player'])
    with score_col2:
        st.metric("Computer Score", st.session_state.score['computer'])
    
    # Display the last game details
    st.markdown(f"""
    <div class='result-box' style='background-color: #f0f2f6;'>
        <h3>Last Game</h3>
        <p>You chose: {st.session_state.last_game['player'].upper()}</p>
        <p>Computer chose: {st.session_state.last_game['computer'].upper()}</p>
        <h2>{st.session_state.last_game['result']}</h2>
    </div>
    """, unsafe_allow_html=True)

# Reset button
if st.button("Reset Game"):
    st.session_state.score = {'player': 0, 'computer': 0}
    if 'last_game' in st.session_state:
        del st.session_state.last_game
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("### How to Play")
st.markdown("""
1. Choose your move by clicking one of the buttons (Rock, Paper, or Scissors)
2. The computer will randomly select its move
3. The winner is determined by the classic rules:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
4. Keep track of your score and try to beat the computer!
""")
