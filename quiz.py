import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.master.configure(bg="#2C3E50")

        self.questions = questions
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Verdana", 16, "bold"), wraplength=500, justify="center", bg="#2C3E50", fg="white")
        self.question_label.pack(pady=20)

        self.option_var = tk.IntVar()
        self.option_var.set(-1)  # Set an initial value

        self.option_radios = []
        for i in range(4):
            option_radio = tk.Radiobutton(master, text="", variable=self.option_var, value=i + 1, font=("Verdana", 12), bg="#3498DB", fg="white", activebackground="#2980B9", command=self.on_radio_click)
            option_radio.pack(pady=5)
            self.option_radios.append(option_radio)

        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Verdana", 12), bg="#2ECC71", fg="white", padx=10)
        self.next_button.pack(pady=20)

        self.congrats_label = tk.Label(master, text="", font=("Verdana", 20, "bold"), bg="#2C3E50", fg="#2ECC71")
        self.congrats_label.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            self.question_label.config(text=current_question.text)

            for i, (option_radio, option) in enumerate(zip(self.option_radios, current_question.options)):
                option_radio.config(text=option, bg="#3498DB", relief=tk.RAISED)

        else:
            self.show_congrats_page()

    def on_radio_click(self):
        
        selected_option = self.option_var.get()
        for i, option_radio in enumerate(self.option_radios):
            if i + 1 == selected_option:
                option_radio.config(bg="#2E86C1", relief=tk.SUNKEN)
            else:
                option_radio.config(bg="#3498DB", relief=tk.RAISED)

    def next_question(self):
        user_answer = self.option_var.get()

        if user_answer == -1:
            messagebox.showinfo("Error", "Please select an answer.")
            return

        current_question = self.questions[self.current_question_index]
        if current_question.correct_option == user_answer:
            self.score += 1

        self.current_question_index += 1
        self.option_var.set(-1)  

        self.display_question()

        
        self.master.after(200, self.reset_button_color)

    def reset_button_color(self):
        for option_radio in self.option_radios:
            option_radio.config(bg="#3498DB", relief=tk.RAISED)

    def show_congrats_page(self):
        for widget in [self.question_label, self.next_button]:
            widget.pack_forget()

        for option_radio in self.option_radios:
            option_radio.pack_forget()

        congrats_text = f"Congratulations!\nYour score: {self.score}/{len(self.questions)}"
        self.congrats_label.config(text=congrats_text)
        self.congrats_label.pack(pady=20)

def main():
    # Example 
    question1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3)
    question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1)
    question3 = Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], 3)

    questions_list = [question1, question2, question3]

    root = tk.Tk()
    app = QuizApp(root, questions_list)
    root.mainloop()

if __name__ == "__main__":
    main()
