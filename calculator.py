# Simple calculator - CodSoft Task 2

# User input for numbers and operation
n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
# Calculating the result based on the operation
if operation=='+':
    print("Result (Sum):",n1+n2)
elif operation=='-':
    print("Result (Difference):",n1-n2)
elif operation=='*':
    print ("Result (Product):",n1*n2)
elif operation=='/':
    if n2!=0:
        print("Result (Quotient):",n1/n2)
    else:
        print("Error: Division by zero is not allowed.")
# For invalid operation input
else:
    print("Invalid operation.")
    