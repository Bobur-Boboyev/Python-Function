def is_strong_password(password: str):
    return len(password) >= 8

password = input("Enter your password: ")

result = is_strong_password(password)

if result:
    print("strong")
else:
    print("weak")