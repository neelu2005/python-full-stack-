# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

#sum of numbers 1 to 10
i = 1
total = 0
while i <= 10:
    total += i
    i += 1

print(total)

#reverse a number
num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

#break
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#search for a number
numbers = [10, 20, 30, 40, 50]
for x in numbers:
    if x == 30:
        print("Found")
        break

#break with while
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

#simple for else
for i in range(5):
    print(i)
else:
    print("Loop completed")

#for else with break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed")


#break → else will NOT execute
#no break → else WILL execute

#nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)



