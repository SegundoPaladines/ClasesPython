from persona import Persona

# Digo que Profesor es una subclase de persona
class Profesor(Persona):

    #Constructor
    def __init__(self, cedula, nombre, apellido, edad, materia, ieducativa):
        self._materia = materia
        self._ieducativa = ieducativa
        #llamar a la funcion init del padre para que setee los atributos de la persona
        super().__init__(cedula, nombre, apellido, edad)

    #getters y setters
    def get_materia(self):
        return self._materia
    
    def set_masteria(self, materia):
        self._materia = materia

    def get_ieducativa(self):
        return self._ieducativa
    
    def set_ieducativa(self, ieducativa):
        self._ieducativa = ieducativa
    
    def presentarse(self):
        presentacion = "Hola, mi nombre es "+super().get_nombre()+" "+super().get_apellido()
        presentacion += " y dicto la meteria de "+self._materia+" en la "+self._ieducativa
        
        return presentacion
    
    def imprimirProfesor(self):
        return super().imprimirPersona()+" materia: "+self._materia + "Institucion Educativa: "+self._ieducativa