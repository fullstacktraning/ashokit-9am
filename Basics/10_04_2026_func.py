# Function
# Business logic (or) Block of Statements
# reuse the business logic
# def is the keyword, used to declare the function

# Example - 1
# def func_one():
#     pass

# func_one()

# Example - 2
# def func_one():
#     print("welcome to functions !!!")

# func_one()

# Example - 3
# No Parameters - No Return Type
# def addition():
#     num1 = 200
#     num2 = 100
#     res = num1 + num2
#     print(f"Addition :{res}")

# addition()

# Example - 4
# no parameters - with return type
# def subtraction():
#     num1 = 200
#     num2 = 100
#     res = num1 - num2
#     return res

# x = subtraction()
# print(f"Subtraction :{x}")

# Example - 5
# with parameters - no return type
# def multiplication(num1, num2):
#     res = num1 * num2
#     print(f"Multiplication : {res}")

# multiplication(200,100)

# Example - 6
# with parameters - with return type
# def division(num1, num2):
#     res = num1 / num2
#     return res

# x = division(200,100)
# print(x)

# no para  - no return
# no para  - with return type
# with para - no return type
# with para - with return type

# Example - 7
# def db_conn(username,password,db_name):
#     if db_name=="oracle":
#         if username=="scott" and password=="tiger":
#             return "Oracle Connection Soon"
#     elif db_name=="mysql":
#         if username=="admin" and password=="admin@123":
#             return "MySQL Connection Soon"
#     else:
#         return "Conn Err"
    
# conn = db_conn("scott","tiger","oracle")
# print(conn)

# conn1 = db_conn("admin","admin@123","mysql")
# print(conn1)

# Example - 8
# Default Arguments
# def func_one(num1 = 200, num2 = 100):
#     res = num1 + num2
#     print(res)

# func_one()
# func_one(2000,2000)
# func_one(None)

# Example - 9
# def func_one(num1 , num2):
#     print(num1, num2)

# func_one(num2=100, num1=200)


# Example - 10
# variable argument
# *
# data stored -- tuple
# def func_one(*param1):
#     print( sum(param1) )

# func_one(10)
# func_one(10,20,30,40,50)