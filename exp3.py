
#for loop

# Q.1]

n = int(input("Numbers to print :" ))
i = 0
for i in range(1, n+1):
    print (i)

# Q.2]

n = int(input("To print even numbers upto : " ))

i = 0
for i in range(1, n+1):
    if(i%2 == 0):
        print("Even number : ", i)

# Q.3]

n = int(input("To print odd numbers upto : " ))

i = 0
for i in range(1, n+1):
    if(i%2 != 0):
        print("Odd number : ", i)

# Q.4]


n = int(input("Enter the value of n: "))

i = 1
while i <= n * n:
    print(i, end=" ")
    i = i * 2

# Q.5]

n = int(input("Enter the value of n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

 # Q.6]

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact
    sum = sum + sign * term
    sign = sign * -1

print("cos(", x, ") =", sum)

# # Q.7]

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

if root * root != n:
    print("Square root is not a whole number.")
else:
    prime = True

    if root < 2:
        prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

    if prime:
        print(root, "is prime.")
    else:
        print(root, "is not prime.")

# Q.8]


for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

# Q.9]

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# Q.10]

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Q.11]

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Q.12]

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()