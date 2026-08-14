#What is a Function?
#A function is a reusable block of code that performs a specific task.
'''Advantages of Functions
Code reusability
Less code duplication
Better readability
Easy debugging
Easy maintenance
Modular programming'''

#Types of Functions
#Python functions can be broadly classified into:
#Built-in Functions
#Already provided by Python.
'''example: 
print()
input()
len()
type()
sum()
min()
max()
sorted()
abs()
round()'''

'''User-Defined Functions

Functions created by the programmer using def.'''


def welcome():
    print("Welcome to Python")

welcome()

#Creating and Calling a Function
def function_name():
    statements


def greet():
    print("Welcome to Python")

greet()

#Important: Defining a function does not execute it. The function executes only when it is called.

#Function With Parameters

"A parameter is a variable written inside the function definition."
def greet(name, age):
    print("My name is", name)
    print("My age is", age)

greet("Raju", 23)

'''Parameter vs Argument

Parameter → variable in the function definition.

Argument → actual value passed during the function call.'''
def add(a, b):     # a, b → parameters
    print(a + b)

add(10, 20)       # 10, 20 → arguments

#print() vs return

'''This is one of the most important concepts.

Using print()'''
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result)

#using return
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
Remember
'''print()  → displays data
return   → sends data back to caller.'''

#Four Basic Types of Functions
#Functions can be classified based on arguments and return value.
'''Type 1 — No Arguments, No Return'''
def greet():
    print("Welcome")

greet()

'''Type 2 — Arguments, No Return'''
def greet(name):
    print("Welcome", name)

greet("Raju")

'''Type 3 — No Arguments, With Return'''
def get_country():
    return "India"

country = get_country()
print(country)

#Type 4 — Arguments, With Return
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

'''Positional Arguments  :Arguments are assigned according to their position'''
def login(username, password):
    print("Username:", username)
    print("Password:", password)

login("admin", "admin123")

#here:
'''username → "admin"
password → "admin123"'''

#Keyword Arguments :Arguments can be passed using parameter names.

def employee(name, salary):
    print(name)
    print(salary)

employee(salary=50000, name="Rahul")
'''Here the order does not matter because Python matches values using parameter names.'''

#Default Arguments:A parameter can have a default value.
def delivery_charge(charge=40):
    print("Delivery Charge:", charge)

delivery_charge()
delivery_charge(80)
#Important Rule

'''Default parameters should generally come after non-default parameters.'''
def student(name, age=18):
    print(name, age)

'''Variable-Length Arguments — *args
*args is used when we don't know how many positional arguments will be passed.
Python stores them in a tuple.'''
def total_bill(*prices):
    print(prices)

total_bill(500, 1000, 1500)

def total_bill(*prices):
    return sum(prices)

print(total_bill(500, 1000, 1500))

'''Keyword Variable-Length Arguments — **kwargs

**kwargs is used when we don't know how many keyword arguments will be passed.

Python stores them in a dictionary.'''

def profile(**details):
    print(details)

profile(
    name="Teja",
    age=23,
    city="Hyderabad"
)



def product(**details):
    for key, value in details.items():
        print(key, ":", value)

product(
    name="Laptop",
    brand="HP",
    price=65000
)

#trick :
# '''*args     → positional → tuple
#**kwargs  → keyword → dictionary'''

#Multiple Return Values:a function can return multiple values.

def calculate(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction

x, y = calculate(20, 10)

print("Addition:", x)
print("Subtraction:", y)


#Docstring

#A docstring describes what a function does.

def user_info():
    """Display user information."""
    print("User details")


print(user_info.__doc__)

#Docstrings are especially useful in larger projects where multiple developers work with the same code.

# Function Calling Another Function:One function can call another function.

def add(a, b):
    return a + b


def display():
    result = add(10, 20)
    print("Result:", result)


display()

This is useful for breaking a large application into smaller tasks.

#Positional-Only Parameters /

#Parameters before / can only be passed positionally.

def user(name, age, /):
    print(name, age)


user("Jani", 21)

#This will not work:

user(name="Jani", age=21)

#Keyword-Only Parameters *
#Parameters after * must be supplied using keywords.

def user(*, name, age):
    print(name, age)
user(name="Jani", age=21)

#This is invalid:
user("Jani", 21)

# / and * Together

#Python can combine positional-only, normal, and keyword-only parameters.

def student(name, /, age, *, course):
    print(name, age, course)

student("Ravi", 22, course="Python")

#Here:

'''name    → positional-only
age     → positional or keyword
course  → keyword-only'''

#Real-Time Example — Student Result
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3




def calculate_average(total):
    return total / 3




def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"




marks1 = 80
marks2 = 70
marks3 = 90
total = calculate_total(marks1, marks2, marks3)
average = calculate_average(total)
result = check_result(average)
print("Total:", total)
print("Average:", average)
print("Result:", result)

#Output:

'''Total: 240
Average: 80.0
Result: Pass'''

#This demonstrates how separate functions can work together to build a larger application.#
#GitHub README — Day 14

#You can directly use this for your GitHub repository:

# Day 14 — Python Functions


## Topics Covered


'''- Functions
- Built-in Functions
- User-Defined Functions
- Function Definition and Calling
- Parameters and Arguments
- Positional Arguments
- Keyword Arguments
- Default Arguments
- return Statement
- print() vs return
- Four Types of Functions
- Multiple Return Values
- *args
- **kwargs
- Positional-Only Parameters
- Keyword-Only Parameters
- Docstrings
- Function Calling Another Function
- Real-Time Function Examples '''


## 1. Functions


#A function is a reusable block of code that performs a specific task.


#python
def add(a, b):
    return a + b
print(add(10, 20))

'''Output:
30'''

'''Parameters and Arguments

Parameter → Variable in function definition.

Argument → Actual value passed during function call.'''

def greet(name):
    print("Hello", name)
greet("Neelufar")

##print() vs return
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

#print() displays a value, while return sends a value back to the caller.

#Positional Arguments
def student(name, age):
    print(name, age)

student("Ravi", 22)

#Arguments are matched according to their position.

#Keyword Arguments
def employee(name, salary):
    print(name, salary)


employee(salary=50000, name="Rahul")

#Arguments are passed using parameter names.

#Default Arguments
def delivery_charge(charge=40):
    print(charge)
delivery_charge()
delivery_charge(80)

 #*args

#Used to accept a variable number of positional arguments.

def total_bill(*prices):
    return sum(prices)


print(total_bill(500, 1000, 1500))

#Output:
#3000

'''*args stores values in a tuple.

#**kwargs

#Used to accept a variable number of keyword arguments.'''

def profile(**details):
    print(details)


profile(name="Teja", age=23, city="Hyderabad")

#**kwargs stores values in a dictionary.

# Multiple Return Values
def calculate(a, b):
    return a + b, a - b
addition, subtraction = calculate(20, 10)
print(addition)
print(subtraction)


# Docstrings
def welcome():
    """Display a welcome message."""
    print("Welcome to Python")
print(welcome.__doc__)


'''11. Key Takeaways
#Functions improve code reusability.
#def is used to create functions.
#A function executes when it is called.
#Parameters are variables in the definition.
#Arguments are values passed during the call.
#print() displays data.
#return sends data back to the caller.
#Positional arguments depend on order.
#Keyword arguments use parameter names.
#Default arguments provide fallback values.
#*args → positional arguments → tuple.
#**kwargs → keyword arguments → dictionary.
#/ → positional-only parameters.
#* → keyword-only parameters.
#Functions can return multiple values.
#Docstrings describe the purpose of functions.'''
#Core Function Flow:Define → Call → Pass Arguments → Execute → Return Result
