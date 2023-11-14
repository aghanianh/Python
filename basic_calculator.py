import time
def addition(op1, op2):
    return op1 + op2
def substraction(op1, op2):
    return op1 - op2
def division(op1, op2):
    if op2 == 0:
        raise ZeroDivisionError('op2 is 0')
    return op1 / op2
def multiplication(op1, op2):
    return op1 * op2


while True:
    time.sleep(1)
    print("\n\nMenu:")
    print("1.Addition")
    print("2.Substraction")
    print("3.Divison")
    print("4.Multiplication")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice [1,5]: "))
        if choice == 5:
            break
        if choice < 1 or choice > 4:
            print("Invalid choosing")
            continue

        x = float(input("Enter first operant:..."))
        y = float(input("Enter second operant:..."))

        if choice == 1:
            result = addition(x,y)
        elif choice == 2:
            result = substraction(x,y)
        elif choice == 3:
            result = division(x,y)
        elif choice == 4:
            result = multiplication(x, y)
        print("Calculating...")
        time.sleep(1)
        print(f"Result is: {result}")
    except ValueError as ve:
        print(f'error: {ve}')
    except Exception as e:
        print(f'An unexpected error occured: {e}')

