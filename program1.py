a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter the choice (1-4): "))
if c == 1:
    print("Addition:", a + b)
elif c == 2:   
    print("Subtraction:", a - b)
elif c == 3:
    print("Multiplication:", a * b)
elif c == 4:
    print("Division:", a / b)
else:
    print("Invalid choice")