# OOPS - Object Oriented Programming System
# class - collection of variables and functions
# class is the keyword, used to declare the class

# Example-1
# class Test:
#     def wish(self):             # self - current object (Ex this in java)
#         print('welcome to oops !!!')

# t1 = Test()     #creating the object
# t1.wish()       #welcome to oops !!!

# Example-2
# class Test:
#     # no para - no return 
#     def add1(self):
#         num1 = 200
#         num2 = 100
#         res = num1 + num2
#         print(f'Addition : {res}')

#     # no para - with return type
#     def add2(self):
#         num1 = 200
#         num2 = 100
#         res = num1 + num2
#         return res
    
#     # with para - no return type
#     def add3(self,num1,num2):
#         res = num1 + num2
#         print(f'Addition :{res}')

#     # with para - with return type
#     def add4(self,num1,num2):
#         res = num1 + num2
#         return res

# t1 = Test()
# t1.add1()
# x = t1.add2()
# print(f'Addition :  {x}')
# t1.add3(200,100)
# y = t1.add4(200,100)
# print(f'Addition : {y}')

# Example - 3
# Instance Variables
# __init__() called as constructor
# it will execute only once
# when ever we create object, automatically contrsuctor will execute
# class Test:
#     def __init__(self):
#         self.num1 = 10
#         self.num2 = 20

# t1 = Test()
# t2 = Test()
# t1.num1 = 100
# t1.num2 = 200

# print(f't1 object data : {t1.num1}...{t1.num2}')
# print(f't2 object data : {t2.num1}...{t2.num2}')

# Example - 4
# class variables, shared to multiple objects
# class Test:
#     company = "TCS....!"  # class variable

#     def __init__(self,name):
#         self.name = name

# t1 = Test("Emp1")
# print(f'name of the employee {t1.name} and company name {t1.company}')
        
# t2 = Test("Emp2")
# print(f'name of the employee {t2.name} and company name {t2.company}')

# Example - 5
# we can modify class variable with Class Name
# class Test:
#     name = "TCS...!"

# t1 = Test()
# t2 = Test()
# print(f'Name ... {t1.name}')
# print(f'Name...{t2.name}')

# Test.name = "Oracle...!"
# print(f'Name ... {t1.name}')
# print(f'Name...{t2.name}')

# Example - 6
# class Test:
#     name = "Microsoft...!"

# t1 = Test()
# t2 = Test()
# print(f'Name ... {t1.name}')
# print(f'Name...{t2.name}')

# t1.name = "Google" # add instance variable to t1 object
# print(f'Name ... {t1.name}')
# print(f'Name...{t2.name}')

# Example-7
# class Test:
#     company = "TCS...!"
#     def __init__(self,name):
#         self.name = name

#     @classmethod
#     def change_company(cls,new_company):
#         cls.company = new_company

# Test.change_company("Oracle...!")
# t1 = Test("Google")
# t2 = Test("Microsoft")

# print(f'Company ... {Test.company}')
# print(f'Company...{Test.company}')

#Example-8
#first pri - object level, next priority -- class level
# class Test:
#     name = "hello" # class var

#     def __init__(self,name):
#         self.name = name
        

# t1 = Test("Samp1")
# print(t1.name)

#Example-9
#__ is used to declare the private variables
#Encapsulation
#private variables, unable to access outside of class
#private variables, unable to access with class objects
# class Test:
#     def __init__(self):
#         self.__amount = 50000
#     def display_amount(self):
#         return self.__amount
    
# t1 = Test()
# # t1.__amount
# print(t1.display_amount())
# print(t1._Test__amount)

#Example-10
# class Parent:
#     def test1(self):
#         print("Parent...!")

# class Child(Parent):
#     def test2(self):
#         print("Child...!")

# obj = Child()
# obj.test1()
# obj.test2()

#Example-11
#Multi Level
class Parent:
    def test1(self):
        print("Parent....!")

class Child(Parent):
    def test2(self):
        print("Child....!")

class Subchild(Child):
    def test3(self):
        print("Subchild....!")
obj = Subchild()
obj.test1()
obj.test2()
obj.test3()