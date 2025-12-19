def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz!")
    else:
        print("Xato! yana urinib ko'ring.")

secret = 12
guess = int(input("Guess: "))

is_correct = check_guess(secret, guess)

print_result(is_correct)