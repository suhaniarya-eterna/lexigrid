import tkinter as tk
import winsound

root = tk.Tk()
root.title("LexiGrid")
root.geometry("800x600")
root.configure(bg="#20231e")



#replace questions with database
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the largest ocean on Earth?", "Pacific Ocean"),
    ("Who wrote Romeo and Juliet?", "Shakespeare"),
    ("What is the chemical symbol for water?", "H2O")
]

current = 0
score = 0
lives = 3

def submit():
    global current, score, lives

    answer = entry.get().strip()

    if answer == "":
        feedback.config(text="Enter an answer first.")
        return

    if answer.lower() == questions[current][1].lower():
        score += 1
        feedback.config(text="Correct!", fg="green")
        winsound.Beep(800, 150)
        current += 1
    else:
        lives -= 1
        feedback.config(text="Wrong answer. Try again.", fg="red")
        winsound.Beep(400, 200)

    entry.delete(0, tk.END)
    status.config(text=f"Score: {score}    Lives: {lives}")

    if lives == 0:
        question.config(text="Game Over!")
        feedback.config(text=f"Final score: {score}")
        entry.config(state="disabled")
        button.config(state="disabled")
        win_image = tk.PhotoImage(file="assets/images (2).png")
        image_label = tk.Label(root, image=win_image, bg="#20231e")
        image_label.image = win_image
        image_label.pack(pady=8)

    elif current == len(questions):
        question.config(text="You won!")
        feedback.config(text=f"Final score: {score}")
        entry.config(state="disabled")
        button.config(state="disabled")
        win_image = tk.PhotoImage(file="assets/images.png")

        image_label = tk.Label(root, image=win_image, bg="#20231e")
        image_label.image = win_image
        image_label.pack(pady=8)

    else:
        question.config(text=questions[current][0])

tk.Label(
    root, text="LEXIGRID",
    font=("Arial", 26, "bold"),
    bg="#20231e", fg="white"
).pack(pady=25)

status = tk.Label(
    root, text="Score: 0    Lives: 3",
    font=("Arial", 14),
    bg="#20231e", fg="white"
)
status.pack(pady=10)

question = tk.Label(
    root, text=questions[0][0],
    font=("Arial", 17),
    wraplength=600,
    bg="#20231e", fg="white"
)
question.pack(pady=35)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)
entry.focus_set()

button = tk.Button(
    root, text="Submit",
    command=submit,
    font=("Arial", 13)
)
button.pack(pady=10)

entry.bind("<Return>", submit)

feedback = tk.Label(
    root, text="Enter your answer",
    font=("Arial", 12),
    bg="#20231e", fg="white"
)
feedback.pack(pady=15)

root.mainloop()
