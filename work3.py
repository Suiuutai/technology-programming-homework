text = "PythonProgramming"
result = text[:6]
print(result)   

word = "Hello"
reversed_word = word[::-1]
print(reversed_word)   

phrase = "abcdefghijklmnop"
result = phrase[::2]
print(result)   

sentence = "DataScience"
result = sentence[-4:]
print(result)   

data = "MachineLearning"
result = data[7:12]
print(result)   

string = "abcdefg"
result = string[0] + string[-1]
print(result)   

word = "Python"
result = word[1:-1]
print(result)   

code = "programming"
result = code[::2]
print(result)   

email = "student@university.com"
start = email.index("@") + 1
end = email.index(".")
result = email[start:end]
print(result)   

palindrome = "madam"
if palindrome == palindrome[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")