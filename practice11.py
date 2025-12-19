def calculate_tax(salary):
    if salary > 5_000_000:
        tax_rate = 0.20
    else:
        tax_rate = 0.13

    return salary * tax_rate


def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax

salary = float(input("Salary: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print(f"Tax amount: {tax}")
print(f"Net salary: {net_salary}")
