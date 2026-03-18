class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def get_best_grade(self):
        return max(self.grades)

    def get_worst_grade(self):
        return min(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calculate_average()}")
        print("--------------------")



class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

    def get_top_student(self):
        best = self.students[0]

        for student in self.students:
            if student.calculate_average() > best.calculate_average():
                best = student

        return best

    def get_lowest_student(self):
        worst = self.students[0]

        for student in self.students:
            if student.calculate_average() < worst.calculate_average():
                worst = student

        return worst

s1 = Student("Aida", 1)
s1.add_grade(90)
s1.add_grade(95)

s2 = Student("Ali", 2)
s2.add_grade(70)
s2.add_grade(60)

s3 = Student("Sara", 3)
s3.add_grade(85)
s3.add_grade(88)

manager = StudentManager()
manager.add_student(s1)
manager.add_student(s2)
manager.add_student(s3)

print("Все студенты:")
manager.display_all_students()
print("Лучший студент:")
top_student = manager.get_top_student()
top_student.display_info()
print("Худший студент:")
worst_student = manager.get_lowest_student()
worst_student.display_info()