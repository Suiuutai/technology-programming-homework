#Задание 1
card = input("Введите номер карты (16 цифр): ")
if len(card) == 16 and card.isdigit():
    masked = "*" * 12 + card[-4:]
    print(masked)
else:
    print("Invalid card number")

#Задание 2
words = ["banana", "apple", "cherry", "grape"]
letter = "a"
result = []
for word in words:
    if word.count(letter) >= 2:
        result.append(word)
if len(result) > 0:
    print(result)
else:
    print("No words found")

#Задание 3
words = ["apple", "banana", "cherry", "blueberry"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("The longest word is", longest)

#Задание 4
sentence = "python is a great programming language"
words = sentence.split()
if len(words) < 2:
    print("Too short to modify")
else:
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].capitalize()
    result = " ".join(words)
    print(result)

#Задание 5
numbers = [1, 2, 2, 3, 4, 4, 5]
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(result)