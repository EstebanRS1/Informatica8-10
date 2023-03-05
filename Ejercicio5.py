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
        self. __registro = "" #os.getcwdb()
        self. __notas = ""
        self. __indice = Indices() ## Solo se guarda un objeto tipo Indices
    
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
        self.__nombre = ""
        self.__cedula = 0
        self.__genero=""
        #self.visita=str
        #Un paciente tiene muchas visitas, en este ejemplo los trabajamos
        #como diccionarios
        self.__visitas={} # Clave-->fecha, valor-->Visita

    def verNombre(self):
        return self.__nombre
    def asignarNombre(self,n):
        self.__nombre=n
    def verCedula(self):
        return self.__cedula
    def asignarCedula(self,c):
        self.__cedula=c
    def verGenero(self):
        return self.__genero
    def asignarGenero(self,g):
        self.__genero=g

    def verVisita(self,f):
        return self.visita.get(f)
    # def verDict_Visitas(self):
    #     return self.dict_Visitas
    def asignarVisita(self,v):
        self.__visitas[v.verFecha]=v

    def verListadoVisitas(self):
        return self.__visitas
    
    def verificarExiste(self,f):
        return f in self.__visitas
    
    def eliminarVisita(self,f):
        del self.__visitas[f]
class Sistema:
    def __init__(self):
        self.__pacientes={}#Clave --> cedula y Valor --> el paciente
    
    def verificarExiste(self,c):
        return c in self.__pacientes
        #     return True
        # else:
        #     return False
    def agregarPaciente(self,p):
        self.__pacientes[p.verCedula()]=p

    def eliminarPac(self,c):
        del self.__pacientes[c]
        return True
    
    def verPac(self,c):
        return self.__pacientes[c]
    
    def cargarGuardar(self):
        pass

def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Error!, Ingrese un dato numérico...")
    return valor

def validarf(cc):
    while True:
        try:
            valor=float(input(cc))
            break
        except ValueError:
            print("Error, ingrese un valor valido")
    return valor
    

def main():
    sis =Sistema()
    while True:
        print("Ingrese: \n1. Nuevo Paciente \n2. Editar Paciente \n3. Eliminar Paciente \n4. Cargar/Guardar \n5. Ver cantidad de visitas de pacientes \n6.Salir")
        valor=validar("Valor: ")

        if valor == 1:
            cedula= validar("Ingrese la Cedula: ")
            if sis.verificarExiste(cedula) == True:
                print(f"El Paciente ya esta en el sistema... Verifique la cedula registrada {cedula}")
                continue
            else:
                p = Paciente()
                p.asignarCedula(cedula)
                p.asignarNombre(input("Ingrese el Nombre: "))
                p.asignarGenero(input("Ingrese el Genero: "))
                numVis=validar(f"Ingrese el numero de visitas que va ingresar el paciente {p.verNombre()}: ")

                for i in range(numVis):
                    dia=validar("Ingrese el dia de la visita: ")
                    mes=validar("Ingrese el mes de la visita: ")
                    año=validar("Ingrese el año de la visita: ")
                    f=datetime.date(año,mes,dia)

                    if p.verificarExiste(f):
                        print("La fecha de la visita ya existe...")
                        continue
                    else:
                        v = Visita()
                        v.asignarFecha(f)
                        v.asignarRegistro(os.getcwd()+f'\Pacientes_{p.verCedula()}')
                        v.asignarNotas(input("Ingrese las observaciones de la visita: "))
                        ind=v.verIndice()
                        ind.asignatPot_A1(validarf("Ingrese el indice de a1: "))
                        ind.asignatPot_A2(validarf("Ingrese el indice de a2: "))
                        ind.asignatPot_B(validarf("Ingrese el indice de b: "))
                        ind.asignatPot_G(validarf("Ingrese el indice de g: "))
                        ind.asignatPot_D(validarf("Ingrese el indice de d: "))
                        ind.asignatPot_T(validarf("Ingrese el indice de t: "))
                        v.asignarIndice(ind)  # Reasigno el objeto indice a la visita                   

                        p.asignarVisita(v)

                sis.agregarPaciente(p)
                print("Paciente agregado con exito...")


        elif valor == 2: #Editar paciente y eliminar visita
            cedula= validar("Ingrese la Cedula: ")

            if sis.verificarExiste(cedula):
                pac=sis.verPac(cedula)
                opcion = validar("Ingresar parar editar:\n1- Nombre\n2- Cédula\n3- Género\n4- Visita\n5- Salir\n Opción:  ")
                if opcion == 1:
                    pac.asignarNombre(input("Ingrese el nuevo nombre: "))
                    print("Nombre actualizado con exito...")
                elif opcion == 2:
                    pac.asignarCedula(validar("Ingrese la nueva cedula: "))
                    sis.eliminarPac(cedula)#Elimino el paciente con la cedula anterior
                    sis.agregarPaciente(pac)#Agrego el paciente con la cedula nueva
                    print("Cedula actualizada con exito...")
                elif opcion == 3:
                    pac.asignarGenero(input("Ingrese el nuevo genero: "))
                    print("Genero actualizado con exito...")
                elif opcion == 4:
                    dia = validar("Ingrese dia:")
                    mes = validar("Ingrese mes:")
                    año = validar("Ingrese año:")
                    f = datetime.datetime(año, mes, dia)

                    if pac.verificarExiste(f)== True:
                        visi=pac.verVisita(f)
                        opcion2 = validar("Ingresar parar editar:\n1- Fecha\n2- Registro\n3- Notas\n4- Indice\n5- Eliminar Visita\n Opción:  ")
                        if opcion2 == 1:
                            dia = validar("Ingrese dia:")
                            mes = validar("Ingrese mes:")
                            año = validar("Ingrese año:")
                            f = datetime.datetime(año, mes, dia)
                            visi.asignarFecha(f)#Reasigno la fecha
                            pac.ingresarVisita(visi)#Reasigno la visita con la fecha nueva
                            pac.eliminarVisita(f)#Elimino la visita con la fecha anterior
                            print("Fecha actualizada con exito...")
                        elif opcion2 == 2:
                            visi.asignarRegistro(input("Ingrese el nuevo registro: "))
                            print("Registro actualizado con exito...")
                        elif opcion2 == 3:
                            notaExistente = visi.verNotas()
                            visi.asignarNotas(input("Ingrese nueva Nota complementaria: ")+notaExistente) 
                            print("Notas actualizadas con exito...")
                        elif opcion2 == 4:
                            indi=visi.verIndice()
                            indi.asignatPot_A1(validarf("Ingrese el indice de a1: "))
                            indi.asignatPot_A2(validarf("Ingrese el indice de a2: "))
                            indi.asignatPot_B(validarf("Ingrese el indice de b: "))
                            indi.asignatPot_G(validarf("Ingrese el indice de g: "))
                            indi.asignatPot_D(validarf("Ingrese el indice de d: "))
                            indi.asignatPot_T(validarf("Ingrese el indice de t: "))
                            visi.asignarIndice(indi)
                            print("Indice actualizado con exito...")
                        elif opcion2 == 5:
                            pac.eliminarVisita(f)# o visi.verFecha()
                            print("Visita eliminada con exito...")
            else:
                print(f"Paciente con cedula {cedula} no existe en el sistema")
        
        elif valor == 3:
            cedula= validar("Ingrese la Cedula: ")
            if sis.verificarExiste(cedula):
                sis.eliminarPac(cedula)
                print("Paciente eliminado con exito...")
            else:
                print(f"Paciente con cedula {cedula} no existe en el sistema")

        elif valor == 4: # Cargar y guardar inforamacion a archivo txt
            cedula= validar("Ingrese la Cedula: ")
            if sis.verificarExiste(cedula):
                p = sis.verPac(cedula)
                archivo = open(f"Paciente {p.verNombre()}.txt",'w')
                archivo.write(p.verNombre()+ "\n" )
                archivo.write(str(p.verCedula())+ "\n" )
                archivo.write(p.verGenero()+ "\n" )
                for i in p.verListadoVisitas():
                    archivo.write(p.verVisita(i).verFecha()+ "\n" )
                    archivo.write(p.verVisita(i).verRegistro()+ "\n" )
                    archivo.write(p.verVisita(i).verNotas()+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_A1())+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_A2())+ "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_B()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_D()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_G()) + "\n" )
                    archivo.write(str(p.verVisita(i).verIndice().verPot_T()) + "\n") 
                archivo.close()
                print("Archivo creado con exito...")

        elif valor == 5: 
            cedula= validar("Ingrese la Cedula: ")
            if sis.verificarExiste(cedula):
                p = sis.verPac(cedula)
                cv =len(p.verListadoVisitas())
                print(f"El paciente {p.verNombre()} tiene {cv} visitas")

        elif valor == 6:
            print("Gracias por usar el sistema...")
            break

        else:
            print("Opción no valida, intente de nuevo...")
if __name__ == "__main__":
    main()