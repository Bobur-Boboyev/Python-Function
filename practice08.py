def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fehrenheit = c_to_f(10)
celsius = f_to_c(50)

print(fehrenheit)
print(celsius)