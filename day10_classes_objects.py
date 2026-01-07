class Student:
    # Attributes,Methods/Functions
    Academy="ASD Academy"  #Class Attribute
    location="Kota"

    #Functions
    # def __init__(self):
    #     print("Constructor is called")
       
    def __init__(self,name):
        print("Constructor is called")
        self.name=name

    def display(self):
        print(f"My name is {self.name} and i am studying at {self.Academy} ")

    def second(self):
        print("This is second function")
        print("Mutiple Lines")
# obj1=Student()
obj1=Student("Rameshwar")   #Creating an Object
obj2=Student("Ajaz")
obj3=Student("Prayank")
# obj1.name="Rameshwar"
# obj2.name="Prayank"
obj1.display()
obj2.display()
obj3.display()
# asif.display()
# print(asif.name)
# print(asif.location)
# asif.second()
# obj2.display()
# obj2.second()
# print(obj1.name)
# obj1.age=58 #Object Attribute
# obj2.name="Rameshwar" #Object Attribute
# print(obj2.name)
# print(obj1.age)
# obj2.hobbies="Cricket"  #Object attribute
# print(obj2.hobbies)