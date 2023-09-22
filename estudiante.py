from persona import Persona

#Digo que el estudiante hereda de persona
class Estudiante(Persona):

    #Constructor
    def __init__(self, cedula, nombre, apellido, edad, carrera ,materias):
        self._materias = materias
        self._carrera = carrera
        super().__init__(cedula, nombre, apellido, edad)

    def get_carrera(self):
        return self._carrera

    def add_materia(self, materia):
        self._materias.append(materia)
    
    def quit_materia(self, materia):
        for asignatura in self._materias:
            if(asignatura.get_nombre() == materia):
                return asignatura
            
        return False
    
    def presentarse(self):
        return super().presentarse() + ", estudio "+self._carrera
    
    def imprimirEstudiante(self):
        return super().imprimirPersona() + " carrera: "+self._carrera