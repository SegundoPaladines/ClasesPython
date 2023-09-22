class Persona:

    #Constructor
    def __init__(self, cedula, nombre, apellido, edad):
        #Un atributo privado se dentota de la siguiente manera self._atributo
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #Getters y setters, no coloco el set_cedula porque no se me da la gana
    def get_cedula(self):
        return self._cedula
    
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido
    
    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad

    #Una funcion pues
    def presentarse(self):
        return "Hola, mi nombre es "+self._nombre+" "+self._apellido+" y tengo "+self._edad+" años"
    
    def imprimirPersona(self):
        return "Cedula: "+self._cedula+" nombre: "+self._nombre+" apellido: "+self._apellido+" edad "+self._edad