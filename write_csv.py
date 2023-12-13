import csv, graficas
from datetime import datetime

def graficar(mes, suma_ingresos, suma_gastos):
    labels = ['Ingresos', 'Gastos']
    valores = [suma_ingresos, suma_gastos]
    
    
    print(f'\nSuma de ingresos para el mes  ({mes}): {suma_ingresos}')
    print(f'Suma de gastos para el mes  ({mes}): {suma_gastos}')
    print(f'tu balance del mes es ({mes}):', suma_ingresos - suma_gastos)
    
    try:
        graficas.generate_bar_chart(labels, valores)
    except Exception as e:
        print(f"Error al generar el gráfico: {e}")

def agregar_ingreso(fecha, ingresos, tipo, comentarios):
    with open('contabilidad.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)

        # Si el archivo está vacío, escribe los encabezados
        if archivo_csv.tell() == 0:
            escritor_csv.writerow(['Fecha', 'Ingresos', 'Tipo Ingresos', 'Comentarios', 'Gastos', 'Tipo Gastos', 'Comentarios'])

        # Escribe una fila con los ingresos y la fecha
        escritor_csv.writerow([fecha, ingresos, tipo, comentarios, None, None, None])

def agregar_gasto(fecha, gastos, tipo, comentarios):
    with open('contabilidad.csv', 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)

        # Si el archivo está vacío, escribe los encabezados
        if archivo_csv.tell() == 0:
            escritor_csv.writerow(['Fecha', 'Ingresos', 'Tipo Ingresos', 'Comentarios', 'Gastos', 'Tipo Gastos', 'Comentarios'])

        # Escribe una fila con los gastos y la fecha
        escritor_csv.writerow([fecha, None, None, None, gastos, tipo, comentarios])

def leer_contabilidad():
    # Obtiene el mes actual
    mes_actual = datetime.now().strftime('%Y-%m')

    # Inicializa la suma de ingresos y gastos para el mes actual
    suma_ingresos = 0
    suma_gastos = 0

    with open('contabilidad.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        # Lee los encabezados
        encabezados = next(lector_csv)
        print(encabezados)

        # Lee y muestra todas las filas
        for fila in lector_csv:
            print(fila)

            # Verifica si la fila pertenece al mes actual
            fecha = fila[0]  # asume que la fecha de ingresos está en la segunda columna
            if fecha.startswith(mes_actual):
                ingresos = float(fila[1]) if fila[1] else 0
                gastos = float(fila[4]) if fila[4] else 0
                print(f'estos son {ingresos}')

                suma_ingresos += ingresos
                suma_gastos += gastos
                
                
    
    graficar(mes_actual, suma_ingresos, suma_gastos)
    #print(f'\nSuma de ingresos para el mes  ({mes_actual}): {suma_ingresos}')
    #print(f'Suma de gastos para el mes  ({mes_actual}): {suma_gastos}')
    #print(f'tu balance del mes es ({mes_actual}):', suma_ingresos - suma_gastos)
    #graficas.generate_bar_chart(etiquetas, valores)
    

def leer_contabilidad_mes():
    # Solicita al usuario ingresar el mes y el año
    mes_input = input("Ingresa el número del mes (1-12): ")
    anio_input = input("Ingresa el año (ej. 2023): ")

    try:
        # Convierte las entradas a enteros
        mes = int(mes_input)
        anio = int(anio_input)
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return

    # Convierte el mes y año en una cadena con formato 'YYYY-MM'
    mes_anio_str = f'{anio:04d}-{mes:02d}'
    print(mes_anio_str)
    print(type(mes_anio_str))

    # Inicializa la suma de ingresos y gastos para el mes especificado
    suma_ingresos = 0
    suma_gastos = 0

    with open('contabilidad.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        # Lee los encabezados
        encabezados = next(lector_csv)
        print(encabezados)

        # Lee y muestra todas las filas
        for fila in lector_csv:
            print(fila)

            # Verifica si la fila pertenece al mes y año especificados
            fecha = fila[0]  # asume que la fecha de ingresos está en la segunda columna
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')


            if fecha_dt.strftime('%Y-%m') == mes_anio_str:
                ingresos = float(fila[1]) if fila[1] else 0
                gastos = float(fila[4]) if fila[4] else 0

                suma_ingresos += ingresos
                suma_gastos += gastos

    graficar(mes_anio_str, suma_ingresos, suma_gastos)


def leer_contabilidad_anio():
    # Solicita al usuario ingresar el año
    anio_input = input("Ingresa el año (ej. 2023): ")

    try:
        # Convierte las entradas a enteros
        anio = int(anio_input)
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return

    # Convierte el mes y año en una cadena con formato 'YYYY-MM'
    anio_str = f'{anio:04d}'
    print(anio_str)
    print(type(anio_str))

    # Inicializa la suma de ingresos y gastos para el mes especificado
    suma_ingresos = 0
    suma_gastos = 0

    with open('contabilidad.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        # Lee los encabezados
        encabezados = next(lector_csv)
        print(encabezados)

        # Lee y muestra todas las filas
        for fila in lector_csv:
            print(fila)

            # Verifica si la fila pertenece al mes y año especificados
            fecha = fila[0]  # asume que la fecha de ingresos está en la segunda columna
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')


            if fecha_dt.strftime('%Y') == anio_str:
                ingresos = float(fila[1]) if fila[1] else 0
                gastos = float(fila[4]) if fila[4] else 0

                suma_ingresos += ingresos
                suma_gastos += gastos

    graficar(anio_str, suma_ingresos, suma_gastos)






if __name__ == '__main__':

    # Ejemplo de uso
    leer_contabilidad()

    # Ejemplo de uso
    leer_contabilidad_mes()

    leer_contabilidad_anio()