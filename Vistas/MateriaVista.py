class MateriaVista:
    def pedir_id_materia(self):
        return input("Ingrese el id de materia: ")
    
    def pedir_nombre_materia(self):
        return input("Ingrese el nombre de la materia: ")
    
    def pedir_id_correlativa(self):
        return input("Ingrese el id de la materia correlativa: ")
    
    def pedir_cantidad_materias(self):
        return input("Ingrese la cantidad de materias que desea cargar: ")
    
    def materia_agregada_correctamente(self,materia):
        print(f"La materia {materia.get_nombre()} se ha agregado correctamente con el id {materia.get_id()}")

    def mostrar_lista_materias(self,listaMaterias):
        print("|ID|NOMBRE|ID_CORRELATIVA|")
        for materia in listaMaterias:
            print(listaMaterias[materia])
