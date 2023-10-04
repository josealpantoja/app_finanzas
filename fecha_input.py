import time

def imprime_hora_local():
    hora_local = time.localtime()  # Obtiene la estructura de tiempo para la hora local
    
    hora_formateada = time.strftime("%Y-%m-%d %H:%M:%S", hora_local) # Formatea la hora como una cadena

    ano = time.strftime("%Y", hora_local)
    mes = selecciona_mes(hora_local)
    dia = time.strftime("%d", hora_local)

    return hora_formateada, ano, mes, dia

def selecciona_mes(hora_local):
    if time.strftime("%m", hora_local) == '01':
        return 'Enero'
    elif time.strftime("%m", hora_local) == '02':
        return 'Febrero'
    elif time.strftime("%m", hora_local) == '03':
        return 'Marzo'
    elif time.strftime("%m", hora_local) == '04':
        return 'Abril'
    elif time.strftime("%m", hora_local) == '05':
        return 'Mayo'
    elif time.strftime("%m", hora_local) == '06':
        return 'Junio'
    elif time.strftime("%m", hora_local) == '07':
        return 'Julio'
    elif time.strftime("%m", hora_local) == '08':
        return 'Agosto'
    elif time.strftime("%m", hora_local) == '09':
        return 'Septiembre'
    elif time.strftime("%m", hora_local) == '10':
        return 'Octubre'
    elif time.strftime("%m", hora_local) == '11':
        return 'Noviembre'
    else:
        return 'Diciembre'

if __name__ == '__main__':
    fecha, ano, mes, dia = imprime_hora_local()
    
    print(fecha)
    print(ano)
    print(mes)
    print(dia)