import unittest
from estacionamiento import intentarEstacionar

class Test(unittest.TestCase):

##############################################################################
#        PRUEBA FUNCION 1 intentarEstacionar
############################################################################

    #Se omite el primer TDD, funcion vacia
    
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
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
