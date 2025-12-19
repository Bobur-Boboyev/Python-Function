def ask_question(question: str, correct_answer: str):
    user_answer = input(f"{question} ")
    return user_answer

def check_answer(user_answer: str, correct_answer: str):
    return user_answer.lower() == correct_answer.lower()

correct_answer = "xa"

user_answer = ask_question("2 juft sonmi?", correct_answer)
is_correct = check_answer(user_answer, correct_answer)

if is_correct:
    print("Javob to'g'ri")
else:
    print("Javob xato")