#Python Functions: Scope, Recursion & Lambda Functions
#1. Scope in Python
'''Scope defines where a variable can be accessed in a program.

Local Scope — variable declared inside a function.
Global Scope — variable declared outside functions.
global keyword — allows modification of a global variable inside a function.
Nonlocal Scope — used in nested functions to modify a variable from the outer function.
LEGB Rule — Python searches variables in this order:'''
'''Local
Enclosing
Global
Built-in'''

# Local Scope
def student():
    name = "Teja"
    print(name)

student()


# Global Scope
company = "Codegnan"

def display():
    print(company)

display()


# Global Keyword
count = 10

def update():
    global count
    count = 20

update()
print(count)


# Nonlocal Scope
def outer():
    count = 10

    def inner():
        nonlocal count
        count += 5

    inner()
    print(count)

outer()

#Pass by Value & Pass by Reference:Python technically uses Pass by Object Reference. For learning purposes, the notes explain immutable objects as pass-by-value behavior and mutable objects as pass-by-reference behavior.
'''Immutable Objects

#Examples:
#int, float, bool, str, tuple, frozenset, complex

#Changes inside the function do not affect the original value.'''

def update(number):
    number = 100
    print("Inside:", number)

value = 50

update(value)

print("Outside:", value)

#Mutable Objects

Examples:
list, set, dict

#Changes made inside the function can affect the original object.
def update(items):
    items.append("Laptop")
cart = ["Mobile", "Watch"]
update(cart)
print(cart)

'''Recursive Functions
A recursive function is a function that calls itself.
Every recursive function needs:
Base Case — stopping condition
Recursive Call — function calls itself'''
#ex: print 1 to n
def numbers(n):
    if n == 0:
        return

    numbers(n - 1)
    print(n)

numbers(5)


#factorial
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#ex:sum of digits
def sum_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)

print(sum_digits(12345))

#ex:fibinocci
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

'''Anonymous / Lambda Functions

A lambda function is an anonymous function created using the lambda keyword. It is mainly used for short, simple, single-expression operations.'''
#lambda parameters: expression
# Addition
add = lambda a, b: a + b
print(add(10, 20))


# Square
square = lambda x: x ** 2
print(square(5))


# Even or Odd
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(8))


# Maximum
maximum = lambda a, b: a if a > b else b
print(maximum(10, 30))

'''lambda functions are shorter than normal def functions and automatically return the expression's result.'''
#filter() Function

#filter() is used to select elements based on a condition.

#Example — Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

#map() Function:map() applies a transformation to every element in an iterable.
#Example — Square Numbers
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)
#reduce() Function
#reduce() repeatedly applies a function and combines all elements into one final value. It comes from the functools module.

#Example — Sum
#from functools import reduce


numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print(result)

#Output:
15

#Easy way to remember
'''filter() → Select
map()    → Transform
reduce() → Combine

The notes summarize the difference exactly this way: filter() selects elements, map() transforms them, and reduce() combines them into one result.

GitHub README — Ready to Push

You can use this as your Day-15 README.md:

# Day 15 — Python Functions: Scope, Recursion & Lambda Functions'''


- '''Scope in Python
- Local Scope
- Global Scope
- global keyword
- Nonlocal Scope
- LEGB Rule
- Pass by Value & Pass by Reference
- Mutable and Immutable Objects
- Recursive Functions
- Base Case and Recursive Call
- Anonymous / Lambda Functions
- filter()
- map()
- reduce()'''


## 1. Scope


'''Scope determines where a variable can be accessed.


Types:
- Local Scope
- Global Scope
- Nonlocal Scope
- Built-in Scope'''


'''Python follows the LEGB rule:


Local → Enclosing → Global → Built-in


## 2. Pass by Value & Pass by Reference


Python uses Pass by Object Reference.


Immutable objects:
int, float, bool, str, tuple


Mutable objects:
list, set, dict


Changes to mutable objects inside a function can affect the original object.


## 3. Recursive Functions


A recursive function calls itself.


Every recursive function should have:
- Base Case
- Recursive Call'''


### Factorial Example


#python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

#Output:
120

#Lambda Functions

#Lambda functions are anonymous functions used for short operations.

#Syntax:

#lambda parameters: expression

#Example:

square = lambda x: x ** 2
print(square(5))

#Output:
25
#filter()

#Used to select elements based on a condition.

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

#Output:
[2, 4, 6]

# map()

#Used to transform every element.

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)

'''Output:
[1, 4, 9, 16, 25]'''

#reduce()

#Used to combine elements into a single value.

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print(result)

#Output:
15

'''Key Takeaways
Scope controls variable accessibility.
LEGB determines how Python searches for variables.
Mutable and immutable objects behave differently when passed to functions.
Recursion requires a base case.
Lambda functions provide concise one-line functions.
filter() selects data.
map() transforms data.
reduce() combines data.'''


### For your LinkedIn screenshots
'''1. **Scope + LEGB**
2. **Pass by Value/Reference + Recursion**
3. **Lambda + `filter()` + `map()`**
4. **`reduce()` + output**'''



