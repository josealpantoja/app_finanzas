def ingresa(): #con esta función vamos a ingresar los ingresos realizados.
    x = int(input('Ingresa el tipo de gasto que has realizado, teclea un número: 1 - Sueldo | 2 - Freelance | 3 - Pago prestamo | 4 - Inversiones | 5 - Renta'))
    #Seleccionamos el concepto de ingreso
    if x == 1:
        tipo = 'Sueldo'
    elif x == 2:
        tipo = 'Freelance'
    elif x == 3:
        tipo = 'Pago prestamo'
    elif x == 4:
        tipo = 'Inversiones'
    elif x == 5:
        tipo = 'Renta'
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        ingresa()

    gasto = float(input('Ingresa la cantidad del ingreso $')) #ingresamos la cantidad ingresada
    comment = input('Detalle de qué fue tu ingreso... 🤔 ') #ingresamos un comentario sobre el ingreso

    return gasto, tipo, comment

def again_ingresa(): #Esta función es para ingresar otro ingreso
    x = str(input('¿Quieres registrar otro ingreso? Y / N '))
    x = x.upper()
    x = x[0]

    if x == 'Y':
        ingresa()
    elif x == 'N':
        print('No, que no')
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        again_ingresa()
    return x



test = ingresa()
print(test)

again = again_ingresa()
print(again)