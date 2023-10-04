def escribe_entero(para_que): #esta función nos ayuda a escoger numeros enteros
    while True:  # Continuar pidiendo hasta que se ingrese un entero válido
        try:
            entero = int(input(f'{para_que} 👉 '))

            return entero
        except ValueError:
            print(f"Eso no es un número válido. Inténtalo de nuevo.")

def escribe_flotante(para_que): #esta función nos ayuda a escoger numeros flotantes
    while True:  # Continuar pidiendo hasta que se ingrese un flotante válido
        try:
            flotante = float(input(f'{para_que} 👉 '))

            return flotante
        except ValueError:
            print(f"Eso no es un número válido. Inténtalo de nuevo.")

if __name__ == '__main__':

    entero = escribe_entero('escribe un entero')
    flotante = escribe_flotante('escribe un flotante')
    print(f'número entero: {entero}, número flotante: {flotante}')