print("Welcome to the calculator!")
print("In this calculator you can add, subtract, multiply and divide whole numbers and decimals")
num1 = float(input('Write the first number: '))
print()
operacion = str(input('What operation are you going to do? + (add), - (substract), * (multiply), o / (divide): '))
print()
num2 = float(input('Now the second number: '))
print("Loading...")
print()

#Suma
if operacion == '+' or operacion == 'add' or operacion == 'Add':
    resultado = num1 + num2
    sumaerror = False
else:
    sumaerror = True

#Resta

if operacion == '-' or operacion == 'substract' or operacion == 'Substract':
    resultado = num1 - num2
    restaerror = False
else:
    restaerror = True

#Multiplicación

if operacion == '*' or operacion == 'multiply' or operacion == 'Multiply':
    resultado = num1 * num2
    multierror = False
else:
    multierror = True

#División

if operacion == '/' or operacion == 'divide' or operacion == 'Divide':
    resultado = num1 / num2
    divierror = False
else:
    divierror = True

if sumaerror == True and restaerror == True and multierror == True and divierror == True:
    print("Sorry, there was an error")
    print()
    print("If you think it is a code error, create an issue in the Github repository")
    print ("Press enter to close")
    input()
else:
    print ("The result is: ")
    print()
    print (resultado)
    print()
    print ("Is not correct? Create an issue in the Github repository")
    print ("Press enter to close")
    input()