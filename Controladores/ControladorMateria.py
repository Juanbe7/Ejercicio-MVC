import os
import sys
sys.path.append(os.getcwd())

from Vistas.MateriaVista import MateriaVista
from Modelos.Materia import Materia
from Vistas.ExcepcionesVista import ExcepcionesVista

class ControladorMateria:
    def __init__(self,vista=MateriaVista):
        self._vista:MateriaVista=vista
        self._materia:Materia
        self._listaMaterias={}
        self._vistaExcept = ExcepcionesVista()
    def cargar_materia(self):
        try:
            max =int(self._vista.pedir_cantidad_materias())
            for i in range(max):
                try:
                    nombre=self._vista.pedir_nombre_materia()
                    try:
                        idCorrelativa = int(self._vista.pedir_id_correlativa())
                        self._materia=Materia(nombre,idCorrelativa)
                        self._listaMaterias[i]=self._materia
                        self._vista.materia_agregada_correctamente(self._materia)
                    except:
                        self._vistaExcept.formato_incorrecto_int()
                except:
                    self._vistaExcept.formato_incorrecto_string()
        except:
            self._vistaExcept.formato_incorrecto_int()

    def mostrar_materias(self):
        self._vista.mostrar_lista_materias(self._listaMaterias)

    def get_materia_por_id(self,id):
        return self._listaMaterias[id]
    
    def get_materias(self):
        return self._listaMaterias