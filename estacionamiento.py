def reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto):
    newEstadoEstacionamiento = None
    hayPuesto = None
    puestoReservado = None
    newPlacaPuesto = None

    vacio = false
    i = 0
    j = tiempoReservado[1]
    while ((i < len(estadoEstacionamiento)) and (not vacio)):
        if (estadoEstacionamiento[i][j] == 0):
            j = j+1
            vacio = true
            while ((j<=(tiempoReservado[2]))and vacio):
                if (estadoEstacionamiento[i][j] != 0):
                    vacio = false
                else:
                    j = j+1
        else:
            i = i+1
    if vacio:
        newEstadoEstacionamiento = estadoEstacionamiento
        newPlacaPuesto = placaPuesto
        hayPuesto = true
        newPlacaPuesto[placa] = i
        puestoReservado = i
        j= tiempoReservado[1]/30
        while (j< len(newEstadoEstacionamiento[1])):
            if (j<=(tiempoReservado[2]/30)):
                newEstadoEstacionamiento[i][j]=2
            else:
                newEstadoEstacionamiento[i][j]=1
            j = j+1
    else:
        hayPuesto = false



    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'hayPuesto': hayPuesto,
            'puestoReservado': puestoReservado,
            'placaPuesto': newPlacaPuesto,
            }

def intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto):
    newEstadoEstacionamiento = None
    hayPuesto = None
    newPlacaPuesto = None
    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'hayPuesto': hayPuesto,
            'placaPuesto': newPlacaPuesto,
            }

def TiempoaCobrar(estadoEstacionamiento, placa, tiempoSalida, placaPuesto):
    unidadesReservadoNoOcupado = None
    unidadesReservadoOcupado = None
    unidadesOcupado = None
    return {
            'unidadesReservadoNoOcupado': unidadesReservadoNoOcupado,
            'unidadesReservadoOcupado': unidadesReservadoOcupado,
            'unidadesOcupado': unidadesOcupado,
            }

def desocuparPuesto(estadoEstacionamiento, placa, horaSalida, placaPuesto):
    newEstadoEstacionamiento = None
    puestoDesocupado = None
    newPlacaPuesto = None
    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'puestoDesocupado': puestoDesocupado,
            'placaPuesto': newPlacaPuesto,
            }