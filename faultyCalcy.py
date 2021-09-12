""" Q->) design a calculator which will correctly solve all the problem except the following one
 45*3 = 123, 85+2 = 546, 33-23 = 582 | your program should take operator and two numbers as input from the user and then return the result """
try:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    op = input("choose operatot => | +, -, *, /| :")
    if (num1 == 45 and num2 == 3 or num1 == 85 and num2 == 2 or num1 == 33 and num2 == 23):
        if op == "+":
            print(546)
        elif op == "-":
            print(582)
        elif op == "*":
            print(123)
    else:
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
except Exception as e:
    print("Please Enter a Valid Integer Value")