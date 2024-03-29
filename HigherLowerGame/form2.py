import tkinter as tk
from tkinter import ttk
from random import randint

class HigherLowerGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("")
        self.root.geometry("200x150")
        self.root.resizable(False, False)

        # Center form to screen
        window_width = 400
        window_height = 200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"200x150+{x}+{y}")

        self.label = ttk.Label(self.root, text="", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=5)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=5)

        self.lower_button = ttk.Button(self.button_frame, text="Lower", command=self.guess_lower)
        self.lower_button.pack(side="left", padx=10)

        self.higher_button = ttk.Button(self.button_frame, text="Higher", command=self.guess_higher)
        self.higher_button.pack(side="left", padx=10)

        self.score_label = ttk.Label(self.root, text="Score: 0", font=("Helvetica", 10, "bold"))
        self.score_label.pack(pady=5)

        self.number_to_guess = None
        self.score = 0

    def generate_number(self):
        self.number_to_guess = randint(1, 100)
        self.label.config(text=f"{self.number_to_guess}", font=("Helvetica", 24, "bold"))

    def guess_lower(self):
        new_number = randint(1, 100)
        result = "Won" if new_number < self.number_to_guess else "Lost"
        if result == "Won":
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.result_label.config(text=f"Number was: {new_number}. You {result}.", font=("Helvetica", 10, "bold"), foreground="green")
        else:
            self.score_label.config(text=f"You lost. Your score was {self.score}.")
            self.score = 0
            self.result_label.config(text=f"Number was: {new_number}. You {result}.", font=("Helvetica", 10, "bold"), foreground="red")
        self.generate_number()

    def guess_higher(self):
        new_number = randint(1, 100)
        result = "Won" if new_number > self.number_to_guess else "Lost"
        if result == "Won":
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.result_label.config(text=f"Number was: {new_number}. You {result}.", font=("Helvetica", 10, "bold"), foreground="green")
        else:
            self.score_label.config(text=f"You lost. Your score was {self.score}.")
            self.score = 0
            self.result_label.config(text=f"Number was: {new_number}. You {result}.", font=("Helvetica", 10, "bold"), foreground="red")
        self.generate_number()

    def run(self):
        self.generate_number()
        self.root.mainloop()

if __name__ == "__main__":
    game = HigherLowerGame()
    game.run()