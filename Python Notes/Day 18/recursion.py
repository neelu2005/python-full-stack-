# ==========================================
# RECURSIVE FUNCTIONS
# ==========================================

# 1. Factorial using Recursion

def factorial(n):
    if n == 0 or n == 1:       # Base Case
        return 1
    return n * factorial(n - 1)  # Recursive Case


print("Factorial:", factorial(5))
# Output: 120


# 2. Fibonacci using Recursion

def fibonacci(n):
    if n == 0:                 # Base Case
        return 0
    elif n == 1:               # Base Case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci:", fibonacci(6))
# Output: 8


# 3. Sum of Natural Numbers using Recursion

def sum_natural(n):
    if n == 1:                 # Base Case
        return 1
    return n + sum_natural(n - 1)


print("Sum:", sum_natural(5))
# Output: 15


# ==========================================
# PASS BY VALUE / OBJECT REFERENCE
# ==========================================

# 4. Immutable Object (int)

def modify_value(num):
    num += 10
    print("Inside:", num)


x = 5
modify_value(x)
print("Outside:", x)

# Output:
# Inside: 15
# Outside: 5


# 5. Mutable Object (list)

def modify_list(lst):
    lst.append(4)


numbers = [1, 2, 3]
modify_list(numbers)

print(numbers)
# Output: [1, 2, 3, 4]


# 6. Prevent Modification using Copy

def modify_list_copy(lst):
    lst = lst[:]       # Creates a copy
    lst.append(5)
    print("Inside:", lst)


numbers = [1, 2, 3]
modify_list_copy(numbers)

print("Outside:", numbers)
# Output:
# Inside: [1, 2, 3, 5]
# Outside: [1, 2, 3]