def is_valid_phone_number(phone: str):
    count = 0

    for i in phone:
        if i.isdigit():
            count += 1
        
    return count == 9

phone = input("Phone number: ")

result = is_valid_phone_number(phone)

print(result)