def calculate_age(birth_year, current_year):
    age = current_year - birth_year

    if age >= 18:
        print("Siz balog'atga yetgansiz.")
    else:
        print("siz balog'atga yetmagansiz.")
    
    return f'sizning yoshingiz: {age}'

age = calculate_age(2008, 2025)
print(age)