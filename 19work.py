studentsList = [
    {"name": "Alice", "subjects": ("Math", "Physics", "English"), "scores": {"Math": 85, "Physics": 78, "English": 92}},
    {"name": "Bob", "subjects": ("Math", "Biology", "English"), "scores": {"Math": 72, "Biology": 88, "English": 80}},
    {"name": "Charlie", "subjects": ("Math", "Physics", "Chemistry"), "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]

# 1
def display_students(students):
    for student in students:
        print("Name:", student["name"])
        print("Subjects:")
        for subject in student["subjects"]:
            print(subject)
        print()

# 2
def get_average_score(name, students):
    for student in students:
        if student["name"] == name:
            total = 0
            count = 0
            for subject in student["scores"]:
                total = total + student["scores"][subject]
                count = count + 1
            average = total / count
            return average

# 3
def find_top_student(students):
    best_student = ""
    best_average = 0
    for student in students:
        total = 0
        count = 0
        for subject in student["scores"]:
            total = total + student["scores"][subject]
            count = count + 1
        average = total / count
        if average > best_average:
            best_average = average
            best_student = student["name"]
    return best_student

# 4
def failed_students(students, passing_score=50):
    failed = []
    for student in students:
        for subject in student["scores"]:
            score = student["scores"][subject]
            if score < passing_score:
                failed.append(student["name"])
                break
    return failed

display_students(studentsList)

print(get_average_score("Alice", studentsList))
print(find_top_student(studentsList))
print(failed_students(studentsList, 75))