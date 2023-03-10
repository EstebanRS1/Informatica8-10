class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, correo, carrera, matricula):
        super().__init__(nombre, edad, correo)
        self.carrera = carrera
        self.matricula = matricula

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.carrera}")
        print(f"Matrícula: {self.matricula}")

diccionario = {}

estudiante1 = Estudiante("Juan", 20, "juan@mail.com", "Ingeniería", 12345)
estudiante2 = Estudiante("Maria", 22, "maria@mail.com", "Arquitectura", 67890)

diccionario[estudiante1.matricula] = estudiante1
diccionario[estudiante2.matricula] = estudiante2

# Mostrar información de un estudiante en particular
matricula_buscada = 12345
if matricula_buscada in diccionario:
    estudiante_buscado = diccionario[matricula_buscada]
    print("Información del estudiante:")
    estudiante_buscado.mostrar_info()

# Mostrar información de todos los estudiantes en el diccionario
for matricula, estudiante in diccionario.items():
    print(f"Información del estudiante con matrícula {matricula}:")
    estudiante.mostrar_info()
