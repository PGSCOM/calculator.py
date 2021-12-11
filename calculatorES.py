print("¡Bienvenido a la calculadora!")
print("En esta calculadora puedes sumar, restar, multiplicar y dividir números enteros y decimales")
num1 = float(input('Empecemos, escribe el primer número: '))
print()
operacion = str(input('¿Qué operación vas a hacer? + (Suma), - (Resta), * (Multiplicar), o / (Dividir): '))
print()
num2 = float(input('Ahora el segundo número: '))
print("Calculando...")
print()

#Suma
if operacion == '+' or operacion == 'suma' or operacion == 'Suma':
    resultado = num1 + num2
    sumaerror = False
else:
    sumaerror = True

#Resta

if operacion == '-' or operacion == 'resta' or operacion == 'Resta':
    resultado = num1 - num2
    restaerror = False
else:
    restaerror = True

#Multiplicación

if operacion == '*' or operacion == 'multiplicacion' or operacion == 'Multiplicacion' or operacion == 'multiplicar' or operacion == 'Multiplicar' or operacion == 'multiplicación' or operacion == 'Multiplicación':
    resultado = num1 * num2
    multierror = False
else:
    multierror = True

#División

if operacion == '/' or operacion == 'dividir' or operacion == 'Dividir' or operacion == 'division' or operacion == 'Division' or operacion == 'división' or operacion == 'División':
    resultado = num1 / num2
    divierror = False
else:
    divierror = True

if sumaerror == True and restaerror == True and multierror == True and divierror == True:
    print("Lo siento, hubo un error")
    print()
    print("Si crees que es un error del codigo, crea un issue en el repositorio de Github")
    print ("Pulsa enter para cerrar")
    input()
else:
    print ("El resultado es: ")
    print()
    print (resultado)
    print()
    print ("¿No es correcto? Crea un issue en el repositorio de Github")
    print ("Pulsa enter para cerrar")
    input()