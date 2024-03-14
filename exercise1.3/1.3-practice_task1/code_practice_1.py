num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
oper = input("Enter the operator (+ or -): ")

if oper == "+":
    sum1 = num1 + num2
    print(sum1)

elif oper == "-":
    if num1 >= num2:
        diff1 = num1 - num2
        print(diff1)

    else:
        diff2 = num2 - num1
        print(diff2)

else:
    print("Unknown operator")


