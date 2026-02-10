class datos_diccionario:
    def __init__(self):
        self.datos_diccionario = {"1092740182": {"nombre": "andres", "apellido": "osorio", "maquina": ("maquina 1", "maquina 2")}}

    def longitud_diccionario(self):
        longitud = len(self.datos_diccionario)
        return longitud
    
    def limpiar_diccionario(self):
        self.datos_diccionario.clear()

    def copiar_diccionario(self):
        copiar = self.datos_diccionario.copy()
        return copiar
    
    def sacar_elementos(self):
        sacar = self.datos_diccionario.items()
        return sacar

    def devolver_valor(self):
        devolver = self.datos_diccionario.keys()
        return devolver

    def sacar_valores(self):
        dato_valores = self.datos_diccionario.values()
        return dato_valores

    def eliminar_elemento(self):
        eliminar = self.datos_diccionario.popitem()
        return eliminar

    def actualizar_info(self, nuevo_diccionario):
        self.datos_diccionario.update(nuevo_diccionario)

    def imprimir_info(self):
        for clave in self.datos_diccionario.keys():
            print(f"dato info: {self.datos_diccionario[clave]}")