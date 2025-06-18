# class car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year    
#     def display(self):
#         print(f"your car is {self.name} {self.model} of year {self.year}.")
# c = car("Bugatti","Chiron",2018)
# c.display()

# class animal:
#     def __init__(self, name):
#         self.name = name 
#     def display(self):
#         print("b") 
# class human(animal):
#     def display(self):
#         super().display()
# c = human("jash")
# c.display()

# class student:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self._age = age
#         self.__gender = gender
#     def info(self):
#         print(f"My name is {self.name} and I am {self._age} years old. I am a {self.__gender}.")   
#         return self.__gender
# st = student("Jash",18,"Male")
# st.info()

class employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.__salary = salary
        self.role = role

    def describe_role(self):
        print(f"Your role is {self.role}")

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,n_salary):
        self.__salary = n_salary

class manager(employee):
    def __init__(self, name, salary, role="manager"):
        super().__init__(name, salary, role)
    
    def describe_role(self):
        print(f"Your role is {self.role}")

