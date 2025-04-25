# Hangman Game

A classic Hangman game built with Python and Streamlit.

## Made by Rehan Aslam

## Description
This is a web-based implementation of the classic Hangman game. Players try to guess a hidden word by suggesting letters. Each wrong guess brings the hangman closer to completion. The game features a clean, modern interface and includes helpful game instructions.

## Features
- Random word generation
- Visual hangman display
- Letter tracking
- Win/lose conditions
- Play again functionality
- Game instructions
- Responsive design

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## How to Run
Run the following command in your terminal:
```bash
streamlit run app.py
```

## How to Play
1. The game will display a hidden word with underscores representing each letter
2. Enter one letter at a time in the input field
3. You have 6 attempts to guess the word
4. Each wrong guess will add a part to the hangman
5. Win by guessing all the letters before the hangman is complete
6. Click "Play Again" to start a new game

## Technologies Used
- Python
- Streamlit
- random-word package 