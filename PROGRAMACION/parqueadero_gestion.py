from parquedaro import Parqueadero

class Gestion_Parqueadero(Parqueadero):

    def __init__(self,espacios):
        self.espacios = espacios
    
    def consultar_espacios_disponibles(self):
        if self.espacios > 0:
            print("Quedan " + str(self.espacios) + " disponibles.")
        else: 
            self.lleno = True
            print("No quedan espacios disponibles.")

    def ingresar_vehiculo(self):
        if self.espacios > 0:
            self.espacios -=1
            print("Ha ingresado un vehiculo.")
        else:
            print("No se pueden ingresar más vehiculos, no hay espacios disponibles.")
    
    def salida_vehiculo(self):
        self.espacios += 1
        print("Ha salido un vehiculo.")
        
        

parqueadero = Gestion_Parqueadero(9)
parqueadero.consultar_espacios_disponibles()
parqueadero.ingresar_vehiculo()
parqueadero.consultar_espacios_disponibles()



