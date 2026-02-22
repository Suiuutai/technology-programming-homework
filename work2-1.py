system = input("Выберите систему (1 — метрическая кг/м, 2 — американская lbs/in): ")
if system == "1":
    weight = float(input("Введите вес (кг): "))
    height = float(input("Введите рост (м): "))
    bmi = weight / (height ** 2)
elif system == "2":
    weight = float(input("Введите вес (lbs): "))
    height = float(input("Введите рост (in): "))
    bmi = (weight * 703) / (height ** 2)
else:
    print("Неверный выбор системы!")
    exit()  
bmi = round(bmi, 2)
print("\nВаш BMI:", bmi)
if bmi < 18.5:
    print("Недостаток веса")
elif bmi < 25:
    print("Норма")
elif bmi < 30:
    print("Избыточный вес")
else:
    print("Ожирение")



