class base_datos:
    def __init__(self):
        # ARRAY
        self.db_empleado_lista = []

    def agregar_empleado(self, obj_empleado):
        self.db_empleado_lista.append(obj_empleado)
        return True
    
    def guardar_varios_empleados(self, varios_obj):
        self.db_empleado_lista.extend(varios_obj)

    def imprimir_info(self):
        for i in range(len(self.db_empleado_lista)):
           print(self.db_empleado_lista[i].ver_info_empleado())