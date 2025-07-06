while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    n1 = float(num1)
    n2 = float(num2)

    if n1 > n2:
        print(n1, "is bigger than", n2)
    elif n1 < n2:
        print(n2, "is bigger than", n1)
    else:
        print("Both numbers are equal.")
