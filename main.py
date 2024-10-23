def check(no1,no2):
    if ((no1^no2)!=0):
        print("Number is not equal")
    else:
        print("Number is equal")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

check(num1,num2)

