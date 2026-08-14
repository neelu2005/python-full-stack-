#what is nested loop ?
# a loop inside a loop is called a nested loop.
for i in range(3):
    for j in range(3):
        print("*")
#outer loop and inner loop
for i in range(1, 4):
    for j in range(1, 4):
        print("*")

# end="" in Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end="")
    print()
  #Why Do We Use print() After the Inner Loop?
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end="")
    print()

# Print a Square Pattern
for i in range(1, 5):
    for j in range(1, 5):
        print("*", end="")
    print()
#Outer loop = Rows
#Inner loop = Columns
#Print a Rectangle Pattern
for i in range(1, 4):
    for j in range(1, 6):
        print("*", end="")
    print()

#Right-Angled Triangle
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
