"""
How does inheritance work in Python? Give an example demonstrating single and multiple inheritance. - NA
"""

class Students:

    def __init__(self, name, last_name, id):
        self.name = name
        self.last_name = last_name
        self.id = id

    def get_info(self):
        return f'Ism {self.name}, Familya {self.last_name}, Id {self.id}'



studen1 = Students("Ali", "Valiyev", 1)
studen2 = Students("Bilol", "Aliyev", 2)
studen3 = Students("Dilnaz", "Usmonova", 3)


class Student(Students):
    def __init__(self, passport, year):
        super().__init__(self,name='Ali',last_name="Valiyev", id=1)
        self.passport = passport
        self.year = year




print(studen2.get_info())