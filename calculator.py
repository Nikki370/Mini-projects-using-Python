num1 = int(input("Num1: "))
operator = input("operator:")
num2 = int(input("Num2: "))

if operator not in ["+", "-", "/", "*", "%"]:
    print("Invalid input")
elif operator == "+":
    print("Result:",num1+num2)
elif operator == "-":
    print("Result:",num1-num2)
elif operator == "/":
    print("Result:",num1/num2)
elif operator == "*":
    print("Result:",num1*num2)
elif operator == "%":
    print("Result:",num1%num2)



