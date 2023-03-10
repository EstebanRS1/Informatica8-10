# Se requiere un sistema para almacenar y gestionar  la información de puntos de monitoreo meteorológico para  relacionarlos con ciertas enfermedades respiratorias.
# El punto meteorológico tiene información de ubicación, fecha,  y registro de los resultados de contaminantes.

# Le sistema debe permitir solicitar dicha información y almacenarla, igualmente debe permitir la búsqueda y visualización de esta.
import  datetime

# class PMeteorologico():
#     def __init__(self):
        

    
    
   


class Registro():
    def __init__(self):
        self.__nombre=""
        self.__cantidad=0
        self.__registro= 0
        self.__fecha = datetime.datetime.now().strftime("%x")
        self.__ubicacion = ""

        self.__dictContaminantes = {}

    def mostrarNombre(self):
        return self.__nombre
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    def mostrarCantidad(self):
        return self.__cantidad
    def asignarCantidad(self, cantidad):
        self.__cantidad = cantidad
    def mostrarRegistro(self):
        return self.__registro
    def asignarRegistro(self, registro):    
        self.__registro = registro

    def mostrarFecha(self):
        return self.__fecha
    def asignarFecha(self, fecha):
        self.__fecha = fecha

    def mostrarUbicacion(self):
        return self.__ubicacion
    def asignarUbicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def verDictContaminantes(self):
        return self.__dictContaminantes
    def asignarContaminantes(self, contaminante):
        self.__dictContaminantes[contaminante.mostrarRegistro()] = contaminante.mostrarNombre()
    def verContaminante(self,f):
        return self.__dictContaminantes.get(f)
    
    def verificarExiste(self,f):
        return f in self.__dictContaminantes
    
    def eliminarVisita(self,f):
        del self.__dictContaminantes[f]
    
def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("\nError!, Ingrese un dato numérico...")
    return valor


class Sistema():
    def __init__(self):
        self.__dictPMeteorologico = {}

    def verificarExiste(self,c):
        return c in self.__dictPMeteorologico
        #     return True
        # else:
        #     return False
    def agregarPM(self,p):
        self.__dictPMeteorologico[p.mostrarRegistro()]=p

    def eliminarPM(self,c):
        del self.__dictPMeteorologico[c]
        return True
    
    def verPac(self,c):
        return self.__dictPMeteorologico[c]
    
#def main():
sis=Sistema()
while True:
    menu=validar("""
    1. Agregar Punto Meteorológico
    2. Ver Punto Meteorológico
    3. Eliminar Punto Meteorológico
    4. Salir
    
    """)

    if menu==1: #Agregar
           
        rg= Registro()
        rg.asignarRegistro(validar("Ingrese el registro del contaminante: "))
        rg.asignarNombre(input("Ingrese el nombre del contaminante: "))
        rg.asignarCantidad(validar("Ingrese la Cantidad del contaminante: "))
        rg.asignarUbicacion(input("Ingrese la ubicación: "))
        rg.asignarFecha(validar("Ingrese la fecha: "))
        rg.asignarContaminantes(rg)

        sis.agregarPM(rg)
    
        print("Punto Meteorológico agregado con éxito...")
    elif menu==2:#Ver
        registro= validar("Ingrese el numero de Registro que desea ver: ")
        if sis.verificarExiste(registro):
            ver=sis.verPac(registro)
            print(f"Registro: {ver.mostrarRegistro()} - Nombre: {ver.mostrarNombre()} - Cantidad: {ver.mostrarCantidad()} - Fecha: {ver.mostrarFecha()} - Ubicación: {ver.mostrarUbicacion()}")

        else:
            print(f"El registro: {registro} no existe en el sistema")





    elif menu==3:#Eliminar
        registro= validar("Ingrese el numero de Registro: ")
        if sis.verificarExiste(registro):
            sis.eliminarPM(registro)
            print("Registro eliminado con exito...")
        else:
            print(f"El registro: {registro} no existe en el sistema")



    elif menu==4:#Salir
        print("\nGracias por usar el sistema. Salio con Exito")
        break

    else:
        print("\nOpción no valida, intente de nuevo")
# if __name__ == "__main__":
#     main()