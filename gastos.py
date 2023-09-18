def ingresa(): #con esta función vamos a ingresar los gastos realizados.
    x = int(input('Ingresa el tipo de gasto que has realizado, teclea un número: 1 - Comida | 2 - Casa | 3 - Gas / Transporte | 4 - Recreación | 5 - Vicios'))
    #Seleccionamos el concepto de gasto
    if x == 1:
        tipo = 'Comida'
    elif x == 2:
        tipo = 'Casa'
    elif x == 3:
        tipo = 'Transporte'
    elif x == 4:
        tipo = 'Recreación'
    elif x == 5:
        tipo = 'Vicios'
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        ingresa()

    gasto = float(input('Ingresa la cantidad del gasto $')) #ingresamos la cantidad gastada
    comment = input('Escribe en qué gastaste... 🤔 ') #ingresamos un comentario sobre el gasto

    return gasto, tipo, comment

def again_ingresa(): #Esta función es para ingresar un  gasto
    x = str(input('¿Quieres registrar otro gasto? Y / N '))
    x = x.upper()
    x = x[0]

    if x == 'Y':
        print('si que si')
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