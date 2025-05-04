#python calculator

operator = input("Enter an operator(+ - * / ) ")
num1 = float(input("enter the first number "))
num2 = float(input("enter the second number "))

#print(num1 + num2)
if operator == "+":
    result = num1 + num2
    print(round(result , 3))
elif operator == "-":
    result = num1 - num2
    print(round(result , 3))
elif operator == "*":
    result = num1 * num2
    print(round(result , 3))
elif operator == "/":
    result = num1 / num2
    print(round(result , 3))
else:
    print(f"{operator} is not valid operator")