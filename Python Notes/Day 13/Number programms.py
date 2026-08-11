n = int(input("enter n value:"))
original = n
rev = 0
while n> 0:
    r = n% 10
    rev = rev * 10+r
    n = n // 10
print (f"the reverse of {original} is: {rev}")



#check number is palindrome or not
#using while loop
n = int(input("enter number:"))
original =n 
rev=0
while n > 0:
    r=n%10
    rev = rev * 10+r
    n = n//10
if original == rev:
    print(f"given number is palindrome")
else:
    print(f"given numbe is not palindrome")


n = 121

s = str(n)

if s == s[::-1]:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

#Count Even Digits in a Number
#using for loop
n = 123456

s = str(n)

c = 0

for i in s:
    if int(i) % 2 == 0:
        c = c + 1

print("Count of even digits:", c)


#factors of a number
n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
 #count no of factors
 n = int(input("Enter number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

print("Number of factors:", count)

#Armstrong Number
n = int(input("Enter number: "))

original = n
total = 0

while n > 0:
    r = n % 10
    total = total + r ** 3
    n = n // 10

if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#continue statemnt
for i in range(1, 6):

    if i == 3:
        continue

    print(i)

print("end")

#break vs continue
##This is very important for beginners.
#continue
#Skips the current iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
