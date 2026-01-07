# #Single Inheritance
# class Parent:
#     name="ASD Academy"
#     def display(self):
#         print("Parent Class")
# # obj=Parent()
# # obj.display()
# # print(obj.name)
# class Child(Parent):
#     def hello(self):
#         print("Child Class")
# obj=Child()
# obj.hello()
# obj.display()
# print(obj.name)

#Multiple Inheritance
# class Parent1:
#     name="ASD Academy"
#     def display(self):
#         print("Parent Class")
# class Parent2:
#     company="Microsoft"
#     def display_company(self):
#         print("Parent2 Class")
# class Child(Parent1,Parent2):
#     def hello(self):
#         print("Child Class")
# obj=Child()
# obj.display()
# obj.display_company()
# print(obj.company)

#Mutilevel Inheritance
# class A:
#     def display1(self):
#         print("Parent Class")
# class B(A):
#     def display2(self):
#         print("Child Class")
# class C(B):
#     def display3(self):
#         print("Grand Child Class")
# obj=C()
# obj.display1()
# obj.display2()
# obj.display3()

#Super Keyword
# class A:
#     def __init__(self):
#         print("Parent constructor")

#     def display(self):
#         print("Class A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")

#     def display(self):
#         super().display()
#         print("Class B")
       
# b = B()
# b.display()

#Method Overriding
# class A:
#     def display(self):
#         print("Class A")
# class B(A):
#     def display(self):
#         super().display()
#         print("Class B")
# b = B()
# b.display()

# class Dog:
#     def sound(self):
#         print("Bark")
# class Cat:
#     def sound(self):
#         print("Meow")
# for animal in (Dog(), Cat()):  #animal=Dog(),animal=Cat()
#     print("Called")
#     animal.sound()

# class Bank:
#     # money=500 #Public
#     __money=500 #Protected
#     def balance(self):
#         print(self._money)
# obj=Bank()
# obj.__money=750
# print(obj.__money)
# obj.money=800
# obj.balance()


class Geek: 
	def __init__(self, age = 0): 
		self._age = age 
	
	# getter method 
	# def get_age(self): 
	# 	return self._age 
	@property
	def age(self):
		print("Getter is called")
		return self._age
	
	# setter method 
	# def set_age(self, x): 
	# 	self._age = x 
	@age.setter
	def age(self,age):
		print("Setter is called")
		self._age=age
	

raj = Geek() 

# setting the age using setter 
# raj.set_age(21) 
raj.age=21 #

# retrieving age using getter 
# print(raj.get_age()) 

print(raj.age)

# class Geeks: 
# 	def __init__(self): 
# 		self._age = 0
# 	# using property decorator 
# 	# a getter function 
# 	@property
# 	def age(self): 
# 		print("getter method called") 
# 		return self._age 
	
# 	# a setter function 
# 	@age.setter 
# 	def age(self, a): 
# 		if(a < 18): 
# 			raise ValueError("Sorry you age is below eligibility criteria") 
# 		print("setter method called") 
# 		self._age = a 

# mark = Geeks() 

# mark.age = 20

# print(mark.age)