# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class rect(shape):
#     def __init__(self, b, h):
#         self.b = b
#         self.h = h
#     def area(self):
#         return self.b*self.h
# class circle(shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return 3.14*self.r*self.r
# rec = rect(4,5)
# cir = circle(5)
# print(rec.area())
# print(cir.area())

from abc import ABC, abstractmethod
import csv
import os

# Abstract base class
class Person(ABC):
    @abstractmethod
    def display_info(self):
        pass

# Student class (data only)
class Student(Person):
    def __init__(self, name, roll_no, course):
        self.__name = name
        self.__roll_no = roll_no
        self.__course = course

    def get_data(self):
        return {
            'st_name': self.__name,
            'st_roll_no': self.__roll_no,
            'st_course': self.__course
        }

    def display_info(self):
        print(f"{self.__name} having roll number {self.__roll_no} is enrolled in {self.__course}.")

# Manager class (handles data storage and retrieval)
class StudentManager:
    def __init__(self, filename="st_info.csv"):
        self.filename = filename
        self.fieldnames = ['st_name', 'st_roll_no', 'st_course']

    def add_student(self, student):
        file_exists = os.path.exists(self.filename)
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(student.get_data())
        print("Student data saved successfully.")

    def view_all_students(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                print("\nAll Students:")
                for row in reader:
                    print(f"{row['st_name']} having roll number {row['st_roll_no']} is enrolled in {row['st_course']}.")
        except FileNotFoundError:
            print("No student data found.")

    def view_selected_student(self, name):
        found = False
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if name.lower() == row['st_name'].lower():
                        print(f"\n{row['st_name']} having roll number {row['st_roll_no']} is enrolled in {row['st_course']}.")
                        found = True
                        break
            if not found:
                print(f"No record found for student: {name}")
        except FileNotFoundError:
            print("No student data found.")
# Example run
s1 = Student("Jash", 101, "IT")
s2 = Student("Ravi", 102, "CS")

manager = StudentManager()

# Add students
manager.add_student(s1)
manager.add_student(s2)

# View all students
manager.view_all_students()

# View selected student
manager.view_selected_student("ravi")
