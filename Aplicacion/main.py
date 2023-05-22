import os
import sys
sys.path.append(os.getcwd())
pruebaMateria={}
from Controladores.ControladorAlumno import ControladorAlumno
from Controladores.ControladorMateria import ControladorMateria
from Vistas.AlumnoVista import AlumnoVista
from Vistas.MateriaVista import MateriaVista

def cargar_materias():
    vistaMateria = MateriaVista()
    controllerMateria = ControladorMateria(vistaMateria)
    controllerMateria.cargar_materia()
    controllerMateria.mostrar_materias()
    return controllerMateria.get_materias()

def puedo_rendir():
    materiasDisponibles=cargar_materias()
    vistaAlumno = AlumnoVista()
    controllerAlumno = ControladorAlumno(vistaAlumno,materiasDisponibles)
    controllerAlumno.crearAlumno()
    controllerAlumno.cargarMateriasAprobadas()
    controllerAlumno.puedeRendir()

if __name__ =="__main__":
    puedo_rendir()