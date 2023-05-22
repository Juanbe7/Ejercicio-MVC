class AlumnoVista:
    def pedir_nombre_alumno(self):
        return input("Ingrese el nombre del alumno: ")
    
    def pedir_apellido_alumno(self):
        return input("Ingrese el apellido del alumno: ")
    
    def pedir_legajo_alumno(self):
        return input("Ingrese el legajo del alumno: ")
    
    def pedir_id_materia_aprobada(self):
        return input("Ingrese el id de la materia aprobada: ")
    
    def seguir_agregando(self):
        return input("Desea seguir agregando materias aprobadas?[S/N]: ")
    
    def pedir_id_materia(self):
        return input("Ingrese el id de la materia que desea rendir: ")
    
    def mostrar_no_puede_rendir(self):
        print("El alumno no esta habilitado para rendir esta materia")

    def inscripcion_exitosa(self):
        print("Se realizo la inscripcion con exito!")
    
    