import write_csv, tipos_de_numeros


def balance(): #con esta función vamos a ingresar los gastos realizados.
    seleccion = tipos_de_numeros.escribe_entero('Ingresa el tipo de balance que quieres: 1 - Mes Actual | 2 - Mes Específico | 3 - Año ')
    #Seleccionamos el concepto de gasto
    
    

    if seleccion == 1:
        write_csv.leer_contabilidad()
    elif seleccion == 2:
        write_csv.leer_contabilidad_mes()
    elif seleccion == 3:
        write_csv.leer_contabilidad_anio()
    else:
        print('Ingresa una opción válida 🥹')
        print('')
        print('*' * 50)
        balance()



if __name__ == '__main__':
    balance()