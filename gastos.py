import tipos_de_numeros
import fecha_input
import write_csv

def ingresa(): #con esta función vamos a ingresar los gastos realizados.
    seleccion = tipos_de_numeros.escribe_entero('Ingresa el tipo de gasto que has realizado, teclea un número: 1 - Comida | 2 - Casa | 3 - Gas / Transporte | 4 - Recreación | 5 - Vicios')
    #Seleccionamos el concepto de gasto
    
    if seleccion == 1:
        tipo = 'Comida'
    elif seleccion == 2:
        tipo = 'Casa'
    elif seleccion == 3:
        tipo = 'Transporte'
    elif seleccion == 4:
        tipo = 'Recreación'
    elif seleccion == 5:
        tipo = 'Vicios'
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        ingresa()

    gasto = tipos_de_numeros.escribe_flotante('Tecelea tu GASTO')
    #ingresamos el concepto "gasto" verificando que sea un flotante válido desde el modilo tipos_de_numeros función escribe_flotante
    
    comment = input('Escribe en qué gastaste... 🤔 ') #ingresamos un comentario sobre el gasto

    fecha, ano, mes, dia = fecha_input.imprime_hora_local()

    print('')
    print(f'🚨 Se registra el GASTO por concepto de {tipo}, por la cantidad de ${gasto}, el dia {dia} de {mes} del {ano}; comentarios: {comment} 🤓')
    print('')
    print('* ' * 20, '✅', ' *' * 20)
    print('')

    write_csv.agregar_gasto(fecha, gasto, tipo, comment)

    return gasto, tipo, comment, fecha, ano, mes, dia

def again_ingresa(): #Esta función es para ingresar un  gasto
    seleccion = str(input('¿Quieres registrar otro gasto? Y / N '))
    seleccion = seleccion.upper()
    seleccion = seleccion[0]

    if seleccion == 'Y':
        print('si que si')
        ingresa()
    elif seleccion == 'N':
        print('No, que no')
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        again_ingresa()
    return seleccion


if __name__ == '__main__':

    test = ingresa()
    print(test)

    again = again_ingresa()
    print(again)