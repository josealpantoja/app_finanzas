import tipos_de_numeros
import fecha_input
import write_csv

def ingresa(): #con esta función vamos a ingresar los ingresos realizados.
    seleccion = tipos_de_numeros.escribe_entero('Ingresa el tipo de ingreso que has realizado, teclea un número: 1 - Sueldo | 2 - Freelance | 3 - Pago prestamo | 4 - Inversiones | 5 - Renta ')
    
    #Seleccionamos el concepto de ingreso
    
    if seleccion == 1:
        tipo = 'Sueldo'
    elif seleccion == 2:
        tipo = 'Freelance'
    elif seleccion == 3:
        tipo = 'Pago prestamo'
    elif seleccion == 4:
        tipo = 'Inversiones'
    elif seleccion == 5:
        tipo = 'Renta'
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        ingresa()

    ingreso = tipos_de_numeros.escribe_flotante('Tecelea tu INGRESO')
    #ingresamos el concepto "gasto" verificando que sea un flotante válido desde el modilo tipos_de_numeros función escribe_flotante
    
    comment = input('Detalle de qué fue tu ingreso... 🤔 ') #ingresamos un comentario sobre el ingreso

    fecha, ano, mes, dia = fecha_input.imprime_hora_local()

    print('')
    print(f'🚨 Se registra el INGRESO por concepto de {tipo}, por la cantidad de ${ingreso}, el dia {dia} de {mes} del {ano}; comentarios: {comment} 🤓')
    print('')
    print('* ' * 20, '✅', ' *' * 20)
    print('')

    write_csv.agregar_ingreso(fecha, ingreso, tipo, comment)

    return ingreso, tipo, comment, fecha, ano, mes, dia

def again_ingresa(): #Esta función es para ingresar otro ingreso
    seleccion = str(input('¿Quieres registrar otro ingreso? Y / N '))
    seleccion = seleccion.upper()
    seleccion = seleccion[0]

    if seleccion == 'Y':
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