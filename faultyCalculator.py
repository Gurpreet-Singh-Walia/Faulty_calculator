
val1 = int(input("Enter 1st value : "))
val2 = int(input("Enter 2nd value : "))
operation = input("Enter the operation : ")
if val1 == 45 and val2 == 3 and operation == "*":
    print("45 * 3 = 555")
elif val1 == 56 and val2 == 9 and operation == "+":
    print("56 + 9 = 77")
elif val1 == 56 and val2 == 6 and operation == "/":
    print("56 / 6 = 4")
else:
    if operation == "*":
        result = val1 * val2
        print(f"{val1} {operation} {val2} = {result}")
    elif operation == "+":
        result = val1 + val2
        print(f"{val1} {operation} {val2} = {result}")
    if operation == "/":
        result = val1 / val2
        print(f"{val1} {operation} {val2} = {result}")
    