# Rock-Paper-Scissors-game

This is a simple **Rock, Paper, Scissors** game built using Python's `tkinter` library for the GUI and the `Pillow` library for image handling. The game allows users to play against the computer, displaying both the player's and the computer's choices as images. Scores are maintained and displayed during gameplay.

## Features
- Rock, Paper, and Scissors images for both the player and the computer.
- Keeps track of player and computer scores.
- Displays the result of each round.
- Option to reset the scores and start a new game.

## Requirements

To run this project, you need to install the following dependencies:

- `tkinter` (comes pre-installed with Python)
- `Pillow` for image handling

You can install Pillow using pip:

 #pip install Pillow


 ### Notes:
- Replace `path_to_your_screenshot` with the actual path if you include a screenshot.
- Update the image paths in the code based on where your images are located.

self.choice_images = {

    "Rock": r"your_path_to_image/rock.jpeg",
    
    "Paper": r"your_path_to_image/paper.jpeg",
    
    "Scissors": r"your_path_to_image/scissors.jpeg"
}



Usage
Start the game.
Choose between Rock, Paper, or Scissors by clicking the corresponding image.
The computer will randomly select its choice.
The result of the game (win/lose/tie) will be displayed along with updated scores.
You can reset the scores and start a new game by clicking the "New Game" button.

Run the Python file:
python rock_paper_scissors.py

Game Logic:
Rock beats Scissors
Scissors beat Paper
Paper beats Rock
If both player and computer select the same item, it's a tie.


