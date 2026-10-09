import winsound

total_Lives = 3
total_Questions = 5
current_Question = 0 
score = 0 


def play_Correctsound():
    winsound.Beep(660, 120)
    winsound.Beep(880, 180)


def play_Wrongsound():
    winsound.Beep(500, 300)


def play_Gameoversound():
    winsound.Beep(500, 180)
    winsound.Beep(400, 180)
    winsound.Beep(300, 350)

def ask_question(question, answer):
    global current_Question, score, total_Lives
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        play_Correctsound()
        score += 1
    else:
        print("Incorrect! The correct answer was:", answer)
        play_Wrongsound()
        total_Lives -= 1
    current_Question += 1

    if total_Lives == 0:
        play_Gameoversound()
        print("Game Over! You have no lives left.")
        print("Your final score is:", score)
        exit()

#ask_question("What is the capital of France?", "Paris")


def main():
    global current_Question, total_Lives
#replace this mechanism with database questions
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("What is the largest ocean on Earth?", "Pacific Ocean"),
        ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
        ("What is the chemical symbol for water?", "H2O")
        ]
    while current_Question < total_Questions and total_Lives > 0:
        question, answer = questions[current_Question]
        ask_question(question, answer)

    print("Game Over!")
    print("Your final score is:", score)
    print("Lives remaining:", total_Lives)

main()


