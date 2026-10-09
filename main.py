total_Lives = 3
total_Questions = 5
current_Question = 0 
score = 0 

def ask_question(question, answer):
    global current_Question, score, total_Lives
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was:", answer)
        total_Lives -= 1
    current_Question += 1

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