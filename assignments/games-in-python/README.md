
# 📘 Assignment: Games in Python

## 🎯 Objective

Create a classic Hangman game in Python using strings, loops, conditionals, and user input. This assignment helps students practice core programming concepts while building a fun and interactive game.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Build the initial game structure by creating a word list and selecting a random word for the player to guess.

#### Requirements
Completed program should:

- Use a predefined list of words for the game
- Randomly choose one word at the start of the game
- Display a placeholder for each letter, such as `_ _ _ _ _`
- Keep the game state organized and easy to update as the player guesses

### 🛠️ Player Guessing and Progress Tracking

#### Description
Allow the player to enter letters and update the visible word based on correct guesses while tracking incorrect attempts.

#### Requirements
Completed program should:

- Prompt the user to enter a single letter guess
- Check whether the letter is in the secret word
- Reveal matching letters in the correct positions
- Track and display incorrect guesses remaining
- Prevent repeated guesses from counting multiple times

### 🛠️ Win/Lose Logic

#### Description
Finish the game by determining when the player wins or loses and showing the final result clearly.

#### Requirements
Completed program should:

- End the game when the player correctly guesses the entire word
- End the game when the player runs out of allowed attempts
- Display a clear win or lose message at the end
- Show the final secret word when the game ends
