operator = input("input an operator (+ - * /): ")
num1 = float(input("enter the 1st number: "))
num2 = float(input("enter the 2st number: "))
if operator == "+":
 result = num1 + num2
print(round(result, 3))
elif operator == "-":
result = num1 - num2
print(round(result, 3))
    elif operator == "/":
result = num1 / num2
print(round(result, 3))
    elif operator == "*":
result = num1 * num2
print(round(result, 3))
else:
    print(f"{operator} invalid operator")