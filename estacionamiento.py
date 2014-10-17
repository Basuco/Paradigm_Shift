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
    newEstadoEstacionamiento = None
    puestoDesocupado = None
    newPlacaPuesto = None
    
    newEstadoEstacionamiento= list(estadoEstacionamiento)
    puestoDesocupado= placaPuesto[placa]
    newPlacaPuesto=placaPuesto.copy()
    del newPlacaPuesto[placa]
    
    estadoPuesto= estadoEstacionamiento[puestoDesocupado][horaSalida]
    if estadoPuesto == 1:
        newEstadoEstacionamiento[puestoDesocupado][horaSalida]=0
    elif estadoPuesto == 3: 
        newEstadoEstacionamiento[puestoDesocupado][horaSalida]=2

    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'puestoDesocupado': puestoDesocupado,
            'placaPuesto': newPlacaPuesto,
            }