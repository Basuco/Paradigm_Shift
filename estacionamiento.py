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
    return {
            'estadoEstacionamiento': newEstadoEstacionamiento,
            'puestoDesocupado': puestoDesocupado,
            'placaPuesto': newPlacaPuesto,
            }