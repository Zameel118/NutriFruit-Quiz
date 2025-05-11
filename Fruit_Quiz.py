import tkinter as tk
from tkinter import messagebox
import json
import random

class FruitQuiz:
    def __init__(self):
        # Try to load data from file
        try:
            with open("data.txt", "r") as file:
                self.data = json.load(file)
                if len(self.data) < 2:
                    messagebox.showerror("Error", "Not enough fruit in database (minimum 2 required)")
                    return
        except:
            messagebox.showerror("Error", "Missing/Invalid file")
            return

        # Initialize variables
        self.components = ["energy", "fibre", "sugar", "potassium"]
        self.questions_answered = 0
        self.correct_answers = 0

        # Create main window
        self.window = tk.Tk()
        self.window.title("Fruit Nutrition Quiz")
        self.window.geometry("+0+0")

        # Create GUI elements
        self.question_label = tk.Label(
            self.window, 
            text="Which one has more...", 
            pady=10
        )
        self.question_label.pack()

        self.component_label = tk.Label(
            self.window, 
            text="", 
            font=("Arial", 12, "bold"),
            pady=5
        )
        self.component_label.pack()

        # Create button frame
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        self.left_button = tk.Button(
            button_frame,
            text="",
            width=15,
            command=lambda: self.check_answer("left")
        )
        self.left_button.pack(side=tk.LEFT, padx=5)

        tk.Label(button_frame).pack(side=tk.LEFT, padx=5)

        self.right_button = tk.Button(
            button_frame,
            text="",
            width=15,
            command=lambda: self.check_answer("right")
        )
        self.right_button.pack(side=tk.LEFT, padx=5)

        # Show first question
        self.show_question()

        # Start main loop
        tk.mainloop()

    def show_question(self):
        # Select two random different fruits
        self.selected_fruits = random.sample(self.data, 2)
        
        # Select random component to compare
        self.selected_component = random.choice(self.components)
        
        # Update GUI
        self.component_label.config(text=self.selected_component.upper())
        self.left_button.config(text=self.selected_fruits[0]["name"])
        self.right_button.config(text=self.selected_fruits[1]["name"])

    def check_answer(self, choice):
        # Get values to compare
        left_value = self.selected_fruits[0][self.selected_component]
        right_value = self.selected_fruits[1][self.selected_component]
        
        # Determine if answer was correct
        if choice == "left":
            is_correct = left_value >= right_value
        else:
            is_correct = right_value >= left_value

        # Update score
        self.questions_answered += 1
        if is_correct:
            self.correct_answers += 1
            messagebox.showinfo("Correct!", 
                f"You got it right.\nScore: {self.correct_answers}/{self.questions_answered}")
        else:
            messagebox.showerror("Incorrect!", 
                f"You got it wrong.\nScore: {self.correct_answers}/{self.questions_answered}")

        # Show next question
        self.show_question()

if __name__ == "__main__":
    FruitQuiz()
