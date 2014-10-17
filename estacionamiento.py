def intToHour(time):
   posfix = ''

   if time > 12:
       posfix = 'pm'
   else:
       posfix = 'am'

   hour = str(time % 12 + 6)

   if time % 2 == 0:
       minutes = '00'
   else:
       minutes = '30'

   return hour + ':' + minutes + posfix

def reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto):
    newEstadoEstacionamiento = None
    hayPuesto = None
    puestoReservado = None
    newPlacaPuesto = None
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
    newEstadoEstacionamiento= estadoEstacionamiento
    newPlacaPuesto=dict(placaPuesto)
    puestoDesocupado= placaPuesto[placa] #puesto a desocupar
    if puestoDesocupado==None:
        estadoPuesto=-1
    else:
        estadoPuesto= estadoEstacionamiento[puestoDesocupado][horaSalida]
    if estadoPuesto == 1 or estadoPuesto == 3:
        del newPlacaPuesto[placa]
        for x in xrange(horaSalida+1):
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