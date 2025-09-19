
print("Helllo! Welcome to Git:))")

# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y



def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    #print("3. Multiply")
    #print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    while True:
        calculator()
        cont = input("Do you want to perform another calculation? (yes/no): ")
        if cont.lower() != 'yes':
            print("Goodbye!")
            break
