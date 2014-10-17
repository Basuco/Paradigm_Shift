
import unittest
from estacionamiento import reservarPuesto, getNuevoEstacionamiento

class Test(unittest.TestCase):

##############################################################################
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

    def testTiempoACobrar(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()