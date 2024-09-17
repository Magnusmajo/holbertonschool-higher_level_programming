def resta(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Nop, no entre zero')
        return 'Try again'

while True:
    try:
        op1 = int(input('introduce el 1er numero: '))
        op2 = int(input('introduce el 2do numero: '))
        break
    except ValueError:
        print('Los valores introducidos no son correctos')

operacion = input('Introduce la operacion')

if operacion == 'divide':
    print(divide(op1, op2))
elif operacion == 'resta':
    print(resta(op1, op2))
elif operacion == 'mult':
    print(mult(op1, op2))
else:
    print('Operacion no valida')
