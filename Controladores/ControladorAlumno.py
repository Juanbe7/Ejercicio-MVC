import os
import sys
sys.path.append(os.getcwd())

from Modelos.Alumno import Alumno
from Vistas.AlumnoVista import AlumnoVista
from Vistas.ExcepcionesVista import ExcepcionesVista

class ControladorAlumno:

    def __init__(self,vista,listaMaterias):
        self._vista:AlumnoVista=vista
        self._alumno:Alumno
        self._listaMateriasDisponibles:dict=listaMaterias
        self.__vistaExcept = ExcepcionesVista()

    def crearAlumno(self):
        try:
            legajo = self._vista.pedir_legajo_alumno()
            nombre = self._vista.pedir_nombre_alumno()
            apellido=self._vista.pedir_apellido_alumno()
            self._alumno= Alumno(legajo,nombre,apellido)
        except:
            self.__vistaExcept.formato_incorrecto_string()


    def cargarMateriasAprobadas(self):
        salir=0
        while(salir==0):
            try:
                idMateriaAprobada=int(self._vista.pedir_id_materia_aprobada())
                try:
                    self._alumno.set_materiasAprobadas(self._listaMateriasDisponibles[idMateriaAprobada])
                except:
                    self.__vistaExcept.id_incorrecto()
            except:
                self.__vistaExcept.formato_incorrecto_int()
            try:
                respuesta = self._vista.seguir_agregando().upper()
                if respuesta=="N":
                    salir=1
                elif respuesta!="S":
                    self.__vistaExcept.caracter_no_aceptado()
            except:
                self.__vistaExcept.formato_incorrecto_string()

    def puedeRendir(self):
        try:
            idMateria = self._vista.pedir_id_materia()
            if self._alumno.get_materia_aprobada_por_id(int(idMateria)):
                self._vista.inscripcion_exitosa()
            else:
                self._vista.mostrar_no_puede_rendir()
        except:
            self.__vistaExcept.formato_incorrecto_int()


        