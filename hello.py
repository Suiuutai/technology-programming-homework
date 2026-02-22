def calc(num1, num2, operator):
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2

    elif operator == "**":
        return num1 ** num2

    elif operator == "%":
        
        return (num1 / 100) * num2

    else:
        return "Неизвестная операция"


print(calc(2, 9, "+"))     
print(calc(10, 3, "-"))    
print(calc(4, 5, "*"))     
print(calc(10, 2, "/"))    
print(calc(2, 3, "**"))    
print(calc(20, 200, "%"))