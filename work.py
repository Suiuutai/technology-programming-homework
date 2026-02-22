# # Задание 1: Калькулятор скидок
# membership = input("Введите тип членства (золото / серебро / обычный): ").lower()
# amount = float(input("Введите сумму покупки: "))
# discount = 0
# if membership == "золото":
#     if amount > 100:
#         discount = 20
#     else:
#         discount = 10
# elif membership == "серебро":
#     if amount > 100:
#         discount = 15
#     else:
#         discount = 5
# elif membership == "обычный":
#     if amount > 100:
#         discount = 5
#     else:
#         discount = 0
# else:
#     print("Неверный тип членства")
# final_price = amount - (amount * discount / 100)
# print("Скидка:", discount, "%")
# print("Итоговая сумма:", final_price)

# Задание 2: Оценка студента

# score = int(input("Введите оценку (0-100): "))
# if score >= 90:
#     homework = input("Сданы ли все домашние задания? (да/нет): ").lower()
#     if homework == "да":
#         print("Отлично! Оценка: A+")
#     else:
#         print("Хорошая работа, но сдайте все задания! Оценка: A")
# elif 80 <= score <= 89:
#     attendance = input("Посещал ли более 75% занятий? (да/нет): ").lower()
#     if attendance == "да":
#         print("Хорошо! Оценка: B")
#     else:
#         print("Нужно посещать занятия! Оценка: C")
# else:
#     print("Старайтесь лучше!")


# Задание 3: Одобрение кредита

# salary = float(input("Введите вашу зарплату: "))
# rating = int(input("Введите кредитный рейтинг: "))
# if salary > 50000:
#     if rating > 700:
#         print("Кредит одобрен с низкой процентной ставкой.")
#     else:
#         print("Кредит одобрен, но с высокой процентной ставкой.")
# else:
#     if rating > 700:
#         print("Кредит одобрен, но с жёсткими условиями.")
#     else:
#         print("Кредит отклонён из-за низкой зарплаты и рейтинга.")


# Задание 4: Классификация числа

number = int(input("Введите число: "))
if number % 2 == 0:
    if number % 4 == 0:
        print("Число делится на 4")
    else:
        print("Обычное чётное число")
else:
    if number % 5 == 0:
        print("Число делится на 5")
    else:
        print("Просто нечётное число")