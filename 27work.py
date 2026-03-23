from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    @abstractmethod
    def work(self):
        pass
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        
class Developer(Employee):
    def __init__(self, name, age, salary, programing_language):
            super().__init__(name, age, salary)
            self.programing_language = programing_language
    def work(self):
            return f"{self.name} is coding in {self.programing_language}"
        
class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
            super().__init__(name, age, salary)
            self.team_size = team_size
    def work(self):
            return f"{self.name} manages a team of {self.team_size} people"

def show_work(emp):
    print(emp.work())
def show_info(emp):
    emp.display_info()

dev = Developer("Aida", 22, 1700, "Python")
man = Manager("Aidar", 25, 1500, 5)

show_info(dev)
show_work(dev)
print()
show_info(man)
show_work(man)