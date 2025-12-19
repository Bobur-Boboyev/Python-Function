def is_polindrome(text):
    return text.lower() == text.lower()[::-1]

text = input("Text: ")

result = is_polindrome(text)

print(result)