import ingresos, gastos, tipos_de_numeros

def menu():
    while True:

        try:
            seleccion = tipos_de_numeros.escribe_entero('¿Qué quieres hacer? / teclea un número: 1 - Ingreso | 2 - Gasto | 3 - Balance | 4 - Salir')

            if seleccion == 1:
                ingresos.ingresa()
            elif seleccion == 2:
                gastos.ingresa()
            elif seleccion == 3:
                print('hola, aun no tenemos el balance, estamos trabajando, una disculpita')
            elif seleccion == 4:
                break  # Salir del bucle
            else:
                raise ValueError("Opción inválida. Por favor, selecciona una opción válida.")
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    menu()