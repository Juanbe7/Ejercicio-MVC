class Materia:
    id=0
    def __init__(self,nombre,idCorrelativa):
        self._id=Materia.__get_next_id()
        self._nombre=nombre
        self._idMateriaCorrelativa=idCorrelativa

    def set_id(self,nuevoId):
        self._id=nuevoId
    
    def set_nombre(self,nuevoNombre):
        self._nombre=nuevoNombre

    def set_correlativa(self,nuevaCorrelativa):
        self._correlativa

    def get_id(self):
        return self._id
    
    def get_nombre(self):
        return self._nombre

    def get_correlativa(self):
        return self._correlativa

    @classmethod
    def __get_next_id(cls):
        cls.id += 1
        return cls.id
    
    def __str__(self):
        return f"|{self._id}|{self._nombre}|{self._idMateriaCorrelativa}|"
        