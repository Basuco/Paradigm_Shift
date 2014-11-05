
import unittest
from estacionamiento import *

class Test(unittest.TestCase):

############################################################################
#		PRUEBA FUNCION 1 reservarPuesto
############################################################################

    #Se agrego para seguir el orden TDD
    def testreservaPuesto_Cero(self):
        estadoEstacionamiento = [[0]]
        tiempoReservado=(0,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[2]], 'hayPuesto': True, 'puestoReservado': 0, 'placaPuesto': {12: 0}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
    #Se agrego para seguir el orden TDD    
    def testreservaPuesto_Ocu1(self):
        estadoEstacionamiento = [[1]]
        tiempoReservado=(0,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1]], 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))

    #Se agrego para seguir el orden TDD
    def testreservaPuesto_Ocu2(self):
        estadoEstacionamiento = [[2]]
        tiempoReservado=(0,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[2]], 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
        #Se agrego para seguir el orden TDD
    def testreservaPuesto_Ocu3(self):
        estadoEstacionamiento = [[3]]
        tiempoReservado=(0,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[3]], 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))

#Se agrego para seguir el orden TDD
    def testreservaPuesto_CeroConMas(self):
        estadoEstacionamiento = [[0,0],[0,0]]
        tiempoReservado=(0,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[2, 1], [0, 0]], 'hayPuesto': True, 'puestoReservado': 0, 'placaPuesto': {12: 0}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto)) 

#Se agrego para seguir el orden TDD
    def testreservaPuesto_CeroOcuparSegundoSinImportarValor(self):
        estadoEstacionamiento = [[0,2],[0,0]]
        tiempoReservado=(0,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[2, 1], [0, 0]], 'hayPuesto': True, 'puestoReservado': 0, 'placaPuesto': {12: 0}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto)) 

#Se agrego para seguir el orden TDD    
    def testreservaPuesto_Cero2(self):
        estadoEstacionamiento = [[0,0],[0,0]]
        tiempoReservado=(0,1)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[2, 2], [0, 0]], 'hayPuesto': True, 'puestoReservado': 0, 'placaPuesto': {12: 0}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto)) 

#Se agrego para seguir el orden TDD    
    def testreservaPuesto_OcuPrime(self):
        estadoEstacionamiento = [[1,0],[0,0]]
        tiempoReservado=(0,1)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1, 0], [2, 2]], 'hayPuesto': True, 'puestoReservado': 1, 'placaPuesto': {12: 1}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))

#Se agrego para seguir el orden TDD    
    def testreservaPuesto_OcuAmbosFinal(self):
        estadoEstacionamiento = [[0,1],[0,1]]
        tiempoReservado=(0,1)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[0,1],[0,1]], 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
#Malicia   
    def testreservaPuesto_TiempoInicioMayorFinal(self):
        estadoEstacionamiento = [[1]]
        tiempoReservado=(1,0)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1]], 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))

#Malicia   
    def testreservaPuesto_MasTiempoDelValido(self):
        estadoEstacionamiento = [[1]]
        tiempoReservado=(0,4)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1]], 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))

#Malicia   
    def testreservaPuesto_MasTiempoDelValidoExtendido(self):
        self.maxDiff=None
        estadoEstacionamiento = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        tiempoReservado=(0,40)
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': estadoEstacionamiento, 'hayPuesto': False, 'puestoReservado': None, 'placaPuesto': {}}
        self.assertEqual(resul,reservarPuesto(estadoEstacionamiento, tiempoReservado, placa, placaPuesto))
        
############################################################################
#		PRUEBA FUNCION 2 intentarEstacionar
############################################################################

        #Estacionamiento: 1 puesto, Estado: Libre, Hora: 0 == "6:00"
    def testintentarEstacionar_Cero(self):
        estadoEstacionamiento = [[0]]
        horaLlegada = 0  
        placa = 13 
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1]], 'hayPuesto': True, 'placaPuesto': {13: 0}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))

    #Estacionamiento: 1 puesto, Estado: Ocupado, Hora: 0 == "6:00"
    def testintentarEstacionar_Ocu1(self):
        estadoEstacionamiento = [[1]]
        horaLlegada = 0
        placa = 13
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1]], 'hayPuesto': False, 'placaPuesto': {}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))
    
    #Estacionamiento: 1 puesto, Estado: Reservado Desocupado, Hora: 0 == "6:00"
    def testintentarEstacionar_Ocu2(self):
        estadoEstacionamiento = [[2]]
        horaLlegada = 0 
        placa = 13
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[2]], 'hayPuesto': False, 'placaPuesto': {}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))
        
    #Estacionamiento: 1 puesto, Estado: Reservado desocupado, Hora: 0 == "6:00"
    def testintentarEstacionar_Ocu3(self):
        estadoEstacionamiento = [[3]]
        horaLlegada = 0 
        placa = 13
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[3]], 'hayPuesto': False, 'placaPuesto': {}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))   
        
    #Estacionamiento: 2 puestos, Estado: Todos libres, Hora: 1 == "6:30"
    def testintentarEstacionar_LibresHora(self):
        estadoEstacionamiento = [[0,0],[0,0]]
        horaLlegada = 1 
        placa = 13
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[0, 1], [0, 0]], 'hayPuesto': True,'placaPuesto': {13: 0}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))  
        
    #Estacionamiento: 2 puestos, Estado: Hay un puesto Reservado Desocupado a la hora de entrada, Hora: 1 == "6:30"    
    def testintentarEstacionar_OcuparLibre(self):
        estadoEstacionamiento = [[0,2],[0,0]]
        horaLlegada = 1 
        placa = 13
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[0, 2], [0, 1]], 'hayPuesto': True,'placaPuesto': {13: 1}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto)) 
    
    #Estacionamiento: 2 puestos, Estado: Todos ocupados de alguna manera, Hora: 1 == "6:30" 
    def testintentarEstacionar_TodoOcu(self):
        estadoEstacionamiento = [[1,1],[2,3]]
        horaLlegada = 1
        placa = 12
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1, 1], [2, 3]], 'hayPuesto': False, 'placaPuesto': {}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))

    #Malicia   
    def testrintentarEstacionar_MasTiempoDelValido(self):
        estadoEstacionamiento = [[1]]
        horaLlegada = 30
        placa = 13
        placaPuesto={}
        resul = {'estadoEstacionamiento': [[1]], 'hayPuesto': False, 'placaPuesto': {}}
        self.assertEqual(resul,intentarEstacionar(estadoEstacionamiento, placa, horaLlegada, placaPuesto))
        
############################################################################
#		PRUEBA FUNCION 3 tiempoACobrar
############################################################################

    def testTiempoACobrar(self):
        pass

############################################################################
#		PRUEBA FUNCION 4 desocuparPuesto
############################################################################

    def testDesocuparSinPuestoOcupado(self):
        estadoEstacionamientoInicial = [[0 for x in xrange(8)] for x in xrange(5)]
        estadoEstacionamientoFinal = [[0 for x in xrange(8)] for x in xrange(5)] 
        horaSalida=6
        puesto=3
        placa=1234
        placaPuesto={placa:puesto}
        resultado = {
            'estadoEstacionamiento': estadoEstacionamientoFinal,
            'puestoDesocupado': None,
            'placaPuesto': placaPuesto,
            }
        resultadoF=desocuparPuesto(estadoEstacionamientoInicial,placa,horaSalida,placaPuesto)
        self.assertEqual(resultado,resultadoF)
        
    def testDesocuparSinPuestoOcupadoReservado(self):
        estadoEstacionamientoInicial = [[0 for x in xrange(8)] for x in xrange(5)]
        estadoEstacionamientoFinal = [[0 for x in xrange(8)] for x in xrange(5)] 
        horaSalida=6
        puesto=3
        placa=1234
        estadoEstacionamientoInicial[puesto][horaSalida]=2
        placaPuesto={placa:puesto}
        resultado = {
            'estadoEstacionamiento': estadoEstacionamientoInicial,
            'puestoDesocupado': None,
            'placaPuesto': placaPuesto,
            }
        resultadoF=desocuparPuesto(estadoEstacionamientoInicial,placa,horaSalida,placaPuesto)
        self.assertEqual(resultado,resultadoF)
        
    def testDesocuparUnicoPuestoOcupado(self):
        estadoEstacionamientoInicial = [[0 for x in xrange(8)] for x in xrange(5)]
        estadoEstacionamientoFinal = [[0 for x in xrange(8)] for x in xrange(5)] 
        horaSalida=6
        puesto=3
        placa=1234
        estadoEstacionamientoInicial[puesto][horaSalida]=1
        placaPuesto={placa:puesto}
        resultado = {
            'estadoEstacionamiento': estadoEstacionamientoFinal,
            'puestoDesocupado': puesto,
            'placaPuesto': {},
            }
        resultadoF=desocuparPuesto(estadoEstacionamientoInicial,placa,horaSalida,placaPuesto)
        self.assertEqual(resultado,resultadoF)
        
    def testDesocuparUnicoPuestoReservadoOcupado(self):
        estadoEstacionamientoInicial = [[0 for x in xrange(8)] for x in xrange(5)]
        estadoEstacionamientoFinal = [[0 for x in xrange(8)] for x in xrange(5)] 
        horaSalida=6
        puesto=3
        placa=1234
        estadoEstacionamientoInicial[puesto][horaSalida]=3
        placaPuesto={}
        placaPuesto[placa]=puesto
        placaPuesto[placa+1]=puesto-1
        placaPuestoF={}
        placaPuestoF[placa+1]=puesto-1
        estadoEstacionamientoFinal[puesto][horaSalida]=2
        resultado = {
            'estadoEstacionamiento': estadoEstacionamientoFinal,
            'puestoDesocupado': puesto,
            'placaPuesto': placaPuestoF,
            }
        resultadoF=desocuparPuesto(estadoEstacionamientoInicial,placa,horaSalida,placaPuesto)
        self.assertEqual(resultado,resultadoF)
        
    def testDesocuparUnicoPuestoOcupadoTodoElDia(self):
        estadoEstacionamientoInicial = [[0 for x in xrange(8)] for x in xrange(5)] 
        estadoEstacionamientoFinal = [[0 for x in xrange(8)] for x in xrange(5)] 
        horaSalida=6
        puesto=1
        placa=1234
        for x in xrange(horaSalida+1):
            estadoEstacionamientoInicial[puesto][x]=1
        placaPuesto={}
        placaPuesto[placa]=puesto
        placaPuesto[placa+1]=puesto+1
        placaPuestoF={}
        placaPuestoF[placa+1]=puesto+1
        resultado = {
            'estadoEstacionamiento': estadoEstacionamientoFinal,
            'puestoDesocupado': puesto,
            'placaPuesto': placaPuestoF,
            }
        self.assertEqual(resultado,desocuparPuesto(estadoEstacionamientoInicial,placa,horaSalida,placaPuesto))
        
    def testDesocuparPuestoOcupadoTodoElDia(self):
        estadoEstacionamientoInicial = getNuevoEstacionamiento(12)
        estadoEstacionamientoFinal = getNuevoEstacionamiento(12)
        horaSalida=6
        puesto=1
        placa=1234
        for x in xrange(horaSalida+1):
            estadoEstacionamientoInicial[puesto][x]=1
        for x in xrange(12):
            estadoEstacionamientoInicial[puesto+1][x]=1
            estadoEstacionamientoFinal[puesto+1][x]=1
        placaPuesto={}
        placaPuesto[placa]=puesto
        placaPuesto[placa+1]=puesto+1
        placaPuestoF={}
        placaPuestoF[placa+1]=puesto+1
        resultado = {
            'estadoEstacionamiento': estadoEstacionamientoFinal,
            'puestoDesocupado': puesto,
            'placaPuesto': placaPuestoF,
            }
        self.assertEqual(resultado,desocuparPuesto(estadoEstacionamientoInicial,placa,horaSalida,placaPuesto))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()