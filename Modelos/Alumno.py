import os
import sys
sys.path.append(os.getcwd())
from Modelos.Materia import Materia

class Alumno:
    def __init__(self,legajo,nombre,apellido):
        self._legajo=legajo
        self._nombre=nombre
        self._apellido=apellido
        self._materiasAprobadas:Materia = {}

    def set_nombre(self,nuevoNombre):
        self._nombre=nuevoNombre

    def set_legajo(self,nuevoLegajo):
        self._legajo=nuevoLegajo

    def set_nombre(self,nuevoApellido):
        self._nombre=nuevoApellido

    def set_materiasAprobadas(self,materia):
        self._materiasAprobadas[materia.get_id()]=materia

    def get_materiasAprobadas(self):
        return self._materiasAprobadas

    def get_materia_aprobada_por_id(self,id):
        try:
            return self._materiasAprobadas[id]
        except:
            return False