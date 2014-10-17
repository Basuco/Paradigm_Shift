def intToHour(time):

    time = time * 30

    if time % 60 == 0:
        minutes = '00'
    else:
        minutes = '30'

    hour = (time // 60 + 6)

    hour = str(hour)

    return hour + ':' + minutes

def getNuevoEstacionamiento(nroPuestos):
    return [[0 for _ in range(24)] for _ in range(nroPuestos)]


def reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto):
    newEstadoEstacionamiento = None
    hayPuesto = None
    puestoReservado = None
    newPlacaPuesto = None

    vacio = False
    i = 0
    j = tiempoReservado[1]
    while ((i < len(estadoEstacionamiento)) and (not vacio)):
        if (estadoEstacionamiento[i][j] == 0):
            j = j+1
            vacio = True
            while ((j<=(tiempoReservado[2]))and vacio):
                if (estadoEstacionamiento[i][j] != 0):
                    vacio = False
                else:
                    j = j+1
        else:
            i = i+1
    if vacio:
        newEstadoEstacionamiento = estadoEstacionamiento
        newPlacaPuesto = placaPuesto
        hayPuesto = True
        newPlacaPuesto[placa] = i
        puestoReservado = i
        j= tiempoReservado[1]
        while (j< len(newEstadoEstacionamiento[1])):
            if (j<=(tiempoReservado[2])):
                newEstadoEstacionamiento[i][j]=2
            else:
                newEstadoEstacionamiento[i][j]=1
            j = j+1
    else:
        hayPuesto = False



    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'hayPuesto': hayPuesto,
            'puestoReservado': puestoReservado,
            'placaPuesto': newPlacaPuesto,
            }

def intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto):
    newEstadoEstacionamiento = estadoEstacionamiento
    hayPuesto = False
    newPlacaPuesto = placaPuesto

    i=1

    while (i < len(newEstadoEstacionamiento)) and (not hayPuesto):

        if (newEstadoEstacionamiento[i][horaLlegada] == 0):

            newPlacaPuesto[placa] = i
            hayPuesto = True
            newEstadoEstacionamiento[i][horaLlegada] = 1

        else:
            i=i+1

    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'hayPuesto': hayPuesto,
            'placaPuesto': newPlacaPuesto
            }

def TiempoACobrar(estadoEstacionamiento, placa, tiempoSalida, placaPuesto):
    if not(placa in placaPuesto):
        unidadesReservadoNoOcupado = None
        unidadesReservadoOcupado = None
        unidadesOcupado = None
    else:
        puesto = placaPuesto[placa]
        unidadesReservadoNoOcupado = 0
        unidadesReservadoOcupado = 0
        unidadesOcupado = 0
        last = -1
        for estado in estadoEstacionamiento[puesto][tiempoSalida::-1]:
            if estado == 0:
                break
            elif estado == 1:
                if last == 2 or last == 3:
                    break
                unidadesOcupado = unidadesOcupado + 1
            elif estado == 2:
                unidadesReservadoNoOcupado = unidadesReservadoNoOcupado + 1
            elif estado == 3:
                unidadesReservadoOcupado = unidadesReservadoOcupado + 1

            last = estado

    return {
            'unidadesReservadoNoOcupado': unidadesReservadoNoOcupado,
            'unidadesReservadoOcupado': unidadesReservadoOcupado,
            'unidadesOcupado': unidadesOcupado,
            }

def desocuparPuesto(estadoEstacionamiento, placa, horaSalida, placaPuesto):

    newEstadoEstacionamiento= estadoEstacionamiento
    newPlacaPuesto=dict(placaPuesto)
    puestoDesocupado= placaPuesto[placa] #puesto a desocupar
    if puestoDesocupado==None:
        estadoPuesto=-1
    else:
        estadoPuesto= estadoEstacionamiento[puestoDesocupado][horaSalida]
    if estadoPuesto == 1 or estadoPuesto == 3:
        del newPlacaPuesto[placa]
        for x in range(horaSalida+1):
            actual=newEstadoEstacionamiento[puestoDesocupado][x]
            if actual==1:
                newEstadoEstacionamiento[puestoDesocupado][x]=0
            elif actual==3:
                newEstadoEstacionamiento[puestoDesocupado][x]=2

    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'puestoDesocupado': puestoDesocupado,
            'placaPuesto': newPlacaPuesto,
            }

