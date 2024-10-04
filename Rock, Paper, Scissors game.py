import tkinter as tk
from PIL import Image, ImageTk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        root.title("Rock Paper Scissors")
        root.geometry("600x500")  # Increased width to accommodate scores

        self.choices = ["Rock", "Paper", "Scissors"]
        self.choice_images = {
            "Rock": r"C:\ALL folder in dexstop\PycharmProjects\img\rock.jpeg",
            "Paper": r"C:\ALL folder in dexstop\PycharmProjects\img\paper.jpeg",
            "Scissors": r"C:\ALL folder in dexstop\PycharmProjects\img\scissors.jpeg"
        }

        self.user_choice = tk.StringVar()
        self.user_score = 0
        self.computer_score = 0
        self.create_widgets()

    def create_widgets(self):
        # Label for selecting choice
        self.select_label = tk.Label(self.root, text="Select your choice:", font=("Arial", 16, "bold"))
        self.select_label.pack()

        # Button for each choice
        self.user_choice_buttons = []
        for choice in self.choices:
            choice_image = Image.open(self.choice_images[choice])
            choice_image = choice_image.resize((100, 100))
            choice_image = ImageTk.PhotoImage(choice_image)
            button = tk.Button(self.root, image=choice_image, command=lambda choice=choice: self.on_choice(choice))
            button.image = choice_image
            button.pack(side=tk.LEFT, padx=10)
            self.user_choice_buttons.append(button)

        # Labels for user and computer choices
        self.user_choice_image_label = tk.Label(self.root, text="Your choice:", font=("Arial", 14, "bold"))
        self.user_choice_image_label.pack()

        self.computer_choice_label = tk.Label(self.root, text="Computer's choice:", font=("Arial", 14, "bold"))
        self.computer_choice_label.pack()

        self.computer_choice_image_label = tk.Label(self.root, text="Computer's choice:", font=("Arial", 14, "bold"))
        self.computer_choice_image_label.pack()

        # Label for displaying result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=10)

        # Label for displaying scores
        self.score_label = tk.Label(self.root, text="Score:", font=("Arial", 14, "bold"))
        self.score_label.pack()

        self.user_score_label = tk.Label(self.root, text=f"Your score: {self.user_score}", font=("Arial", 14, "bold"))
        self.user_score_label.pack()

        self.computer_score_label = tk.Label(self.root, text=f"Computer's score: {self.computer_score}", font=("Arial", 14, "bold"))
        self.computer_score_label.pack()

        # Play button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_game, font=("Arial", 14, "bold"))
        self.play_button.pack()

        # Reset button
        self.reset_button = tk.Button(self.root, text="New Game", command=self.reset_scores, font=("Arial", 14, "bold"))
        self.reset_button.pack()

    def on_choice(self, choice):
        self.user_choice.set(choice)

    def play_game(self):
        user_choice = self.user_choice.get()
        if user_choice == "":
            self.result_label.config(text="Please select a choice first.", fg="red")
            return

        computer_choice = random.choice(self.choices)

        user_choice_image = Image.open(self.choice_images[user_choice])
        user_choice_image = user_choice_image.resize((100, 100))
        user_choice_image = ImageTk.PhotoImage(user_choice_image)
        self.user_choice_image_label.config(image=user_choice_image)
        self.user_choice_image_label.image = user_choice_image
        self.user_choice_image_label.configure(text=f"Your choice: {user_choice}", fg="black")  # Text above the image

        computer_choice_image = Image.open(self.choice_images[computer_choice])
        computer_choice_image = computer_choice_image.resize((100, 100))
        computer_choice_image = ImageTk.PhotoImage(computer_choice_image)
        self.computer_choice_image_label.config(image=computer_choice_image)
        self.computer_choice_image_label.image = computer_choice_image
        self.computer_choice_image_label.configure(text=f"Computer's choice: {computer_choice}", fg="black")  # Text above the image

        if user_choice == computer_choice:
            result = "It's a tie!"
            color = "purple"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            color = "green"
            self.user_score += 1
        else:
            result = "Computer wins!"
            color = "red"
            self.computer_score += 1

        self.update_scores()
        self.result_label.config(text=result, fg=color)

    def update_scores(self):
        self.user_score_label.config(text=f"Your score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer's score: {self.computer_score}")

    def reset_scores(self):
        self.user_score = 0
        self.computer_score = 0
        self.update_scores()

def main():
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
