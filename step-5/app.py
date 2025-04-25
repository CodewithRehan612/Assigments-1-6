import streamlit as st
import random
import requests

# Initialize session state variables
if 'word' not in st.session_state:
    st.session_state.word = ''
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = set()
if 'wrong_guesses' not in st.session_state:
    st.session_state.wrong_guesses = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'game_won' not in st.session_state:
    st.session_state.game_won = False

# Hangman ASCII art
HANGMAN_STAGES = [
    '''
       +---+
           |
           |
           |
          ===''',
    '''
       +---+
       O   |
           |
           |
          ===''',
    '''
       +---+
       O   |
       |   |
           |
          ===''',
    '''
       +---+
       O   |
      /|   |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ==='''
]

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?length=5,10")
        if response.status_code == 200:
            return response.json()[0]
        else:
            # Fallback to a list of words if API fails
            words = ["python", "streamlit", "hangman", "programming", "computer", "algorithm", "database", "network", "software", "developer"]
            return random.choice(words)
    except:
        # Fallback to a list of words if API fails
        words = ["python", "streamlit", "hangman", "programming", "computer", "algorithm", "database", "network", "software", "developer"]
        return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def reset_game():
    st.session_state.word = get_random_word()
    st.session_state.guessed_letters = set()
    st.session_state.wrong_guesses = 0
    st.session_state.game_over = False
    st.session_state.game_won = False

# Set page config
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🎮",
    layout="centered"
)

# Title and creator info
st.title("🎮 Hangman Game")
st.markdown("### Made by Rehan Aslam")

# Initialize game if not already done
if not st.session_state.word:
    reset_game()

# Display game status
st.markdown("### Word to guess:")
st.markdown(f"## {display_word(st.session_state.word, st.session_state.guessed_letters)}")

# Display hangman
st.text(HANGMAN_STAGES[st.session_state.wrong_guesses])

# Display guessed letters
st.markdown("### Guessed letters:")
st.markdown(", ".join(sorted(st.session_state.guessed_letters)) if st.session_state.guessed_letters else "None")

# Game logic
if not st.session_state.game_over and not st.session_state.game_won:
    # Input for letter guess
    guess = st.text_input("Enter a letter:", max_chars=1).lower()
    
    if guess:
        if guess in st.session_state.guessed_letters:
            st.warning("You already guessed that letter!")
        elif guess in st.session_state.word:
            st.session_state.guessed_letters.add(guess)
            st.success("Correct guess!")
            
            # Check if all letters are guessed
            if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
                st.session_state.game_won = True
        else:
            st.session_state.guessed_letters.add(guess)
            st.session_state.wrong_guesses += 1
            st.error("Wrong guess!")
            
            if st.session_state.wrong_guesses >= 6:
                st.session_state.game_over = True

# Game over messages
if st.session_state.game_over:
    st.error("Game Over! You lost!")
    st.markdown(f"The word was: **{st.session_state.word}**")
    if st.button("Play Again"):
        reset_game()

if st.session_state.game_won:
    st.success("Congratulations! You won!")
    if st.button("Play Again"):
        reset_game()

# Add a footer
st.markdown("---")
st.markdown("### How to Play")
st.markdown("""
1. Try to guess the hidden word by entering one letter at a time
2. You have 6 attempts to guess the word
3. Each wrong guess will add a part to the hangman
4. Win by guessing all the letters before the hangman is complete
""")
