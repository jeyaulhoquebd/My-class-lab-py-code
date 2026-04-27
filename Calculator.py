# This fuction adds two numbers
def add(a,b):
    return a+b

# This function subtracts two numbers
def subtract (a,b):
    return a-b

# This function multiplies two number
def multiply(a,b):
    return a*b

#This function divides two numbers
def divide(a,b):
    return a / b


print("Select Operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #Take input from  the user
    choice = input("Enter choice(1/2/3/4):")

    #Chek if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
        except ValueError:
            print("Invalid input. please enter a number.")
