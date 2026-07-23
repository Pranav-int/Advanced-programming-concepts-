n=(int(input("enter a number")))
if n==0:
    print("number is zero")
else :
    print("non zero number")





n1=(int(input("enter 1st number")))
n2=(int(input("enter 2nd number")))
if n1>n2:
    print("1st number is larger")
else:
    print("2nd number is larger")






n=(int(input("enter a number")))
if n>=0:
    print(n," is positive")
else:
    print(n," is negitive")





x=input("enter a letter")
if x in['a','e','i','o','u']:
     print(x," is a vovel")
else:
     print(x," is consonent")






n=(int(input("enter your score :")))
y=(int(input("enter total marks")))
z=(n/y)*100

if z>=90:
    print("Excillent score!!")
elif z>=80:
    print("very good score!!")
elif z>=70:
    print("Good score!")
elif z>=60:
    print("Average score...")
else:
    print("poor score")






a=(int(input("enter A")))
b=(int(input("enter B")))
c=(int(input("enter C")))

if a>=b and a>=c:
    print(a," is greatest")
elif b>=c and b>=c:
    print(b," is greatest")
else:
    print(c," is greatest")

if a<=b and a<=c:
    print(a," is smallest")
elif b<=c and b<=c:
    print(b," is smallest")
else:
    print(c," is smallest")




a=(int(input("enter a number")))
if a%2==0:
    print("The number",a, " is even")
else:
    print("The number",a, " is Odd")




n=(int(input("enter year")))
if n%4==0:
    print(n,"year is leap")
else:
    print("its a non leap year")