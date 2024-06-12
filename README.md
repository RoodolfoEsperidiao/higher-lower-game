### README for Higher Lower Game

## Introduction
Welcome to the Higher Lower Game! This is a fun and interactive game where you need to guess which of two Instagram accounts has more followers. The game continues as long as you guess correctly, and your score increases with each correct guess. If you guess incorrectly, the game ends and your final score is displayed.

## How to Play
1. **Start the Game**: The game begins by displaying a logo and the details of two contenders (A and B).
2. **Make a Guess**: You need to guess which contender has more followers by typing 'A' or 'B'.
3. **Continue or End**: If you guess correctly, your score increases, and the game continues with the next contender. If you guess incorrectly, the game ends and your final score is shown.

## Features
- **Random Contenders**: The game randomly selects contenders from a predefined list of Instagram accounts.
- **Score Tracking**: Your score is tracked and displayed each time you guess correctly.
- **Replayability**: The game can be played multiple times, challenging you to beat your previous high score.

## Code Overview

### Imports
The game relies on the following imports:
- `random`: For randomly selecting contenders.
- `clear` from `replit`: To clear the console for a smooth user experience.
- `logo` and `vs` from `art`: For displaying the game logo and visual separators.
- `data` from `game_data`: Contains the list of Instagram accounts with their follower counts and descriptions.

### Functions
1. **contender()**: 
   - Returns a random contender from the `data` list.
   
2. **compare(a, b, answer)**:
   - Compares the follower counts of two contenders (`a` and `b`).
   - Returns `True` if the user's guess (`answer`) is correct, otherwise `False`.

3. **game()**:
   - Main function that runs the game.
   - Initializes the score and selects the first contender.
   - Continuously selects new contenders and compares follower counts until the user makes an incorrect guess.
   - Displays the current score after each correct guess and the final score when the game ends.

### Code Example

```python
from art import logo, vs
from game_data import data
import random
from replit import clear

def contender():
    return random.choice(data)

def compare(a, b, answer):
    follow_a = a['follower_count']
    follow_b = b['follower_count']
    if follow_a > follow_b:
        return answer == 'a'
    else:
        return answer == 'b'

def game():
    a = contender()
    play_again = True
    score = 0
    print(logo)
    while play_again:
        b = contender()
        while a == b:
            b = contender()
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if compare(a, b, answer):
            a = b
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            play_again = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
```

## Conclusion
The Higher Lower Game is a simple yet entertaining way to test your knowledge of Instagram influencers and their follower counts. Enjoy playing and try to achieve the highest score possible!
