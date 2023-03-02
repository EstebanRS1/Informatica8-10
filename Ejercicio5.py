import datetime
import os
# from SisteVMultMed import Medicamento
class Paciente:
    def __init__(self):
        self.nombre = ""
        self.cedula = 0
        self.genero=""
        self.visita=str
        self.dict_Visitas={}

class Indices:
    def __init__(self):
        self.__pot_d=0
        self.__pot_t=0
        self.__pot_a1=0
        self.__pot_a2=0
        self.__pot_b=0
        self.__pot_g=0

    def verPot_D(self):
        return self.__pot_d
    def verPot_T(self):
        return self.__pot_t
    def verPot_A1(self):
        return self.__pot_a1 
    def verPot_A2(self):
        return self.__pot_a2
    def verPot_B(self):
        return self.__pot_b
    def verPot_G(self):
        return self.__pot_g
    
    def asignatPot_D(self,p):
        self.__pot_d=p
    def asignatPot_T(self,p):
        self.__pot_t=p
    def asignatPot_A1(self,p):
        self.__pot_a1=p
    def asignatPot_A2(self,p):
        self.__pot_a2=p
    def asignatPot_B(self,p):
        self.__pot_b=p
    def asignatPot_G(self,p):
        self.__pot_g=p

class Visita:
    def __init_ (self):
    #Atributos de la clase
        self.__fecha = datetime.datetime.now().strftime("%x")
        self. __registro = os.getcwdb()
        self. __notas = ""
        self. __indice = Indices()
    #Metodos de la clase        
    def verfecha(self):
        return self.__fecha
    def verRegistro(self):
        return self. __registro
    def verNotas(self):
        return self.__notas
    def verIndice(self):
        return self.__indice
    
    def asignarRegistro(self,r):
        self.__registro=r
    def asignarNotas(self,n):
        self.__notas=n
    def asignarIndice(self,i):
        self.__indice=i
    def asignarFecha(self,f):
        self.__fecha=f

class Paciente:
    def __init__(self):
        self.nombre = ""
        self.cedula = 0
        self.genero=""
        self.visita=str
        self.dict_Visitas={}
    def verNombre(self):
        return self.nombre
    def verCedula(self):
        return self.cedula
    def verGenero(self):
        return self.genero
    # def verVisita(self):
    #     return self.visita
    # def verDict_Visitas(self):
    #     return self.dict_Visitas
    
    def asignarNombre(self,n):
        self.nombre=n
    def asignarCedula(self,c):
        self.cedula=c
    def asignarGenero(self,g):
        self.genero=g
    def asignarVisita(self,v):
        self.visita=v
    def asignarDict_Visitas(self,d):
        self.dict_Visitas=d
    
class Sistema:
    def __init__(self):
        self.__Pacientes={}
    
    def verificarExiste(self,c):
        if c in self.__Pacientes:
            return True
        else:
            return False
    def agregarPaciente(self,p):
        self.__Pacientes[p.verCedula()]=p

    def eliminarPac(self,c):
        del self.__Pacientes[c]
        return True
    
    def recuperarPac(self,c):
        return self.__Pacientes[c]
    
    def cargarGuardar(self):
        pass
    def validar(self,c):
        while True:
            try:
                valor=int(input(c))
                return valor
            except:
                print("Error, ingrese un valor valido")
        
def main():
    sis =Sistema()
    while True:
        print("Ingrese: \n1. Nuevo Paciente \n2. Editar Paciente \n3. Eliminar Paciente \n4. Cargar/Guardar \n5. Salir")
        valor=sis.validar("Valor: ")

        if valor == 1:
            cedula= sis.validar("Ingrese la Cedula: ")
            if sis.verificarExiste(cedula) == True:
                print(f"El Paciente ya esta en el sistema... Verifique la cedula registrada {cedula}")
                continue

if __name__ == "__main__":
    main()