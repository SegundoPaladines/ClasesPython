from persona import Persona
from profesor import Profesor
from estudiante import Estudiante
import subprocess
import time
import sys

#Listas
personas = []
estudiantes = []
profesores = []

#Funcion principal
def main():
    escribir("Hola, bienvenido al programa de profesores y alumnos \n")
    listarComandos()
    control = True
    while(control):
        control = inicio()

def inicio():
    comando = input("esperando comando $: ")
    
    if(comando == "create persona"):
        crearPersona()

    elif(comando == "create profesor"):
        crearProfesor()
    
    elif(comando == "create estudiante"):
        crearEstudiante()

    elif(comando == "ls personas"):
        listarPersonas()

    elif(comando == "ls profesores"):
        listarProfesores()
    
    elif(comando == "ls estudiantes"):
        listarEstudiantes()

    elif(comando == "ls personas"):
        print("listar personas")

    elif(comando == "ls profesores"):
        print("lsitar profesores")
    
    elif(comando == "ls estudiantes"):
        print("listar estudiante")

    elif(comando == "quit" or comando == "ex" or comando == "exit" or comando == "q"):
        escribir("Hasta la proxima! \n")
        return False
    
    elif(comando == "help"):
        listarComandos()

    elif(comando == "presentar persona"):
        presentarPersona()

    elif(comando == "presentar profesor"):
        presentarProfesor()

    elif(comando == "presentar estudiante"):
        presentarEstudiante()

    elif(comando == "hola"):
        escribir("Hola, un gusto saludarte!\n")
    
    else:
        escribir("Comando desconocido, remitiendo al bash ... \n")
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, text=True)
        print(resultado.stdout)

    return True

def crearPersona():
    cedula = input("cedula: ")
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = input("edad: ")
    
    personas.append(Persona(cedula, nombre, apellido, edad))

def crearProfesor():
    cedula = input("cedula: ")
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = input("edad: ")
    materia = input("Materia que dicta: ")
    ieducativa = input("Insttitución educativa donde trabaja: ")

    profesores.append(Profesor(cedula, nombre, apellido, edad, materia, ieducativa))

def crearEstudiante():
    cedula = input("cedula: ")
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = input("edad: ")
    carrera = input("Carrera que cursa: ")

    estudiantes.append(Estudiante(cedula, nombre, apellido, edad, carrera, []))

def listarPersonas():
    print("Lista de personas:")
    for persona in personas:
        print (persona.imprimirPersona())

def listarProfesores():
    print("Lista de profesores:")
    for profesor in profesores:
        print (profesor.imprimirProfesor())

def listarEstudiantes():
    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        print (estudiante.imprimirEstudiante())

def presentarPersona():
    cedula = input("cedula: ")

    for persona in personas:
        if(persona.get_cedula() == cedula):
            escribir(persona.presentarse()+"\n")
            return True

    print("La cedula especificada no corresponde a ninguna persona")

def presentarProfesor():
    cedula = input("cedula: ")

    for profesor in profesores:
        if(profesor.get_cedula() == cedula):
            escribir(profesor.presentarse()+"\n")
            return True

    print("La cedula especificada no corresponde a ningun profesor")

def presentarEstudiante():
    cedula = input("cedula")

    for estudiante in estudiantes:
        if(estudiante.get_cedula() == cedula):
            escribir(estudiante.presentarse()+"\n")
            return True

    print("La cedula especificada no corresponde a ningun estudiante")


def listarComandos():
    escribir("Listado de comandos: \n")
    escribir("create persona <- crear una persona\n")
    escribir("create profesor <- crear un profesor\n")
    escribir("create estudiante <- crear un estudiante\n")
    escribir("ls personas <- listar personas\n")
    escribir("ls profesores <- listar profesores\n")
    escribir("ls estudiantes <- listar estudiantes\n")
    escribir("presentar persona <- la persona se presenta\n")
    escribir("presentar profesor <- el profesor se presenta\n")
    escribir("presentar estudiante <- el estudiante se presenta\n")
    escribir("help <- lista de comandos\n")

def escribir(cadena):
    for caracter in cadena:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(0.025)

##LLamar al main
if __name__ == main():
    main()

