
import sys

def reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto):
    hayPuesto = None
    puestoReservado = None
    
    newEstadoEstacionamiento = estadoEstacionamiento
    newPlacaPuesto = placaPuesto
    
    

    vacio = False
    if ((tiempoReservado[0]>tiempoReservado[1])or (tiempoReservado[1]>= len(estadoEstacionamiento[0]))):
        valido = False
    else:
        valido = True
    i = 0
    j = tiempoReservado[0]
    while ((i < len(estadoEstacionamiento)) and (not vacio) and (valido)):
        if (estadoEstacionamiento[i][j] == 0):
            j = j+1
            vacio = True
            while ((j<=(tiempoReservado[1]))and vacio):
                if (estadoEstacionamiento[i][j] != 0):
                    vacio = False
                else:
                    j = j+1
        else:
            i = i+1
    if vacio:

        hayPuesto = True
        newPlacaPuesto[placa] = i
        puestoReservado = i
        j= tiempoReservado[0]
        while (j< len(newEstadoEstacionamiento[0])):
            if (j<=(tiempoReservado[1])):
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
    newEstadoEstacionamiento = None
    hayPuesto = None
    newPlacaPuesto = None
    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'hayPuesto': hayPuesto,
            'placaPuesto': newPlacaPuesto,
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
                    break;
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
    newEstadoEstacionamiento = None
    puestoDesocupado = None
    newPlacaPuesto = None
    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'puestoDesocupado': puestoDesocupado,
            'placaPuesto': newPlacaPuesto,
            }

def intToHour(time):
    posfix = ''

    time = time * 30

    if time % 60 == 0:
        minutes = '00'
    else:
        minutes = '30'

    hour = (time // 60 + 6)

    hour = str(hour)

    return hour + ':' + minutes + posfix

if __name__ == "__main__":

    if len(sys.argv) > 1:
        numeroPuestos = sys.argv[1]
    else:
        
        estadoEstacionamiento = [[0,0],[0,0]]
        tiempoReservado=(0,1)
        placa = 12
        placaPuesto={}
        resultado=None
        resultado = reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto)
        print resultado
