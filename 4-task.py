"""
What is the purpose of the __init__ method in Python classes? Provide an example. - NA

"""
class Student:

    def __init__(self, name, last_name, id): # Constructor __init__ class ichida birinchi ishlashini taminlaydi
        self.name = name
        self.last_name = last_name
        self.id = id

studen1 =Student("Ali", "Valiyev", 1)
studen2 =Student("Bilol", "Aliyev", 2)
studen3 =Student("Dilnaz", "Usmonova", 3)

print(studen1.name)
print(studen2.last_name)
print(studen3.id)