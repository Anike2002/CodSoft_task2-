print("Welcome to the Simple calculator")

def addition(num1,num2,):
    add = num1 + num2
    return add
    
def subtraction(num1,num2):
    subtract = num1 - num2
    return subtract

def multiplication(num1,num2):
    multiply = num1 * num2
    return multiply

def division(num1,num2):
    divide = num1 / num2
    return divide

def result():
    return result

operation1 = "add"
print("1 :",operation1)
operation2 = "subtract"
print("2 :",operation2)
operation3 = "multiply"
print("3 :",operation3)
operation4 = "divide"
print("4 :",operation4)

while True:
    num1 = float(input("Enter your first number :"))
    num2 = float(input("Enter your second number :"))
    option = int(input("Choose an option(1,2,3,4) :"))

    if option == 1:
        result = num1 + num2
        print("Result of add is {}".format(result))
    elif option == 2:
        result = num1 - num2
        print("Result of subtract is {}".format(result))
    elif option == 3:
        result = num1 * num2
        print("Result of multiply is {}".format(result))
    elif option == 4:
        result = num1 / num2
        print("Result of divide is {}".format(result))
    else:
        print("You have selected invalid option . Please select from (1,2,3,4) ")

    next_calculation = input("Do you want perform another calculation (yes/no) :")
    if next_calculation != "yes":
        print("Thanks for using calculator")
        break

    