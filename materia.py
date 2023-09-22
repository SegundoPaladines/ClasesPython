class Materia:

    #Constructor
    def __init__(self, nombre, profesor):
        self._nombre = nombre
        self._profesor = profesor

    #Getters y setters
    def get_nombre(self):
        return self._nombre
    
    def get_profesor(self):
        return self._profesor
    
    def set_profesor(self, profesor):
        self._profesor = profesor

    def imprimirMateria(self):
        return "nombre: "+self._nombre+" \nProfesor:\n"+self.imprimirProfesor()