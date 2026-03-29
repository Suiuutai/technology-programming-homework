import math
import datetime

sqrt_25 = math.sqrt(25)
pi_value = math.pi
cos_45 = math.cos(math.radians(45))

with open("results.txt", "w") as f:
    f.write(f"Square root of 25: {sqrt_25}\n")
    f.write(f"Pi value: {pi_value}\n")
    f.write(f"Cosine of 45 degrees: {cos_45}\n")

try:
    with open("results.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found!")

now = datetime.datetime.now()

with open("results.txt", "a") as f:
    f.write(f"\nCurrent date and time: {now}\n")