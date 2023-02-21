class Mascota:
    def __init__(self):
        self.__nombre="hola"
        self.__historia=""
        self.__peso=0
        self.__medicamento=""
        self.__fecha_ingreso=""
    
    #Getters
    def verNombre(self):
        return self.__nombre
    
    def verHistoria(self):
        return self.__historia
    
    def verPeso(self):
        return self.__peso

    def verMedicamento(self):
        return self.__medicamento
    
    def verFecha(self):
        return self.__fecha_ingreso
    
    #Setters
    def asignarNombre(self,N):
        self.__nombre=N

    def asignarHistoria(self,H):
        self.__historia=H

    def asignarMedicamento(self,M):
        self.__medicamento=M

    def asignarFecha(self,F):
        self.__fecha_ingreso=F

    def asignarPeso(self,P):
        self.__peso=P

