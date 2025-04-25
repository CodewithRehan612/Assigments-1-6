# Guess the Number Game

A fun and interactive number guessing game built with Python and Streamlit. The computer generates a random number between 1 and 100, and you have to guess it!

## Features

- Interactive web interface
- Real-time feedback on your guesses
- Hint system to help you narrow down the number
- Attempt counter
- Play again functionality
- Modern and responsive design

## Setup

1. Make sure you have Python installed on your system
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the application:
   ```
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)
3. Enter your guess in the input field
4. Click "Submit Guess" to check your guess
5. Use the "Get a Hint" button if you need help
6. Try to guess the number in as few attempts as possible!

## Game Rules

- The computer generates a random number between 1 and 100
- You need to guess this number
- After each guess, you'll get feedback if your guess was too high or too low
- You can use the hint system to get a range where the number might be
- The game keeps track of your attempts
- Once you guess correctly, you can play again! 