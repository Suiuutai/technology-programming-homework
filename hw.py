class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.course_list = []

    def introduce(self):
        print(f"Hello, my name is {self.name}. I study {self.major}.")

    def major_info(self):
        print(f"My major is {self.major}")

    def gpa_info(self):
        print(f"My GPA is {self.gpa}")

    def courses(self):
        print("Courses:", self.course_list)

    def add_course(self, course):
        self.course_list.append(course)
        print(f"Course {course} added")

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"GPA updated to {self.gpa}")

    def is_honor(self):
        if self.gpa > 3.5:
            print("Student is Honor")
        else:
            print("Student is not Honor")

s1 = Student("Aida", 20, "Computer Science", 3.6)
s1.introduce()
s1.major_info()
s1.add_course("Python")
s1.add_course("Algorithms")
s1.courses()
s1.gpa_info()
s1.update_gpa(3.8)
s1.is_honor()