import string


class Cliente:
    def __init__(self, nombre):
        # Completar
        self.nombre = nombre
        self.siguiente = None
        
        pass


    def __str__(self):
        # NO MODIFICAR
        return self.nombre

class FilaPizza:
    def __init__(self):
        # Completar
        self.primer_nodo = None
        self.ultimo_nodo = None
        self.largo = 0
        
        pass


    def llega_cliente(self, cliente: Cliente):
        # Completar
        
        if self.primer_nodo == None:
            self.primer_nodo = cliente
            self.ultimo_nodo = cliente

        else:
            self.ultimo_nodo.siguiente = cliente
            self.ultimo_nodo = cliente

        self.largo += 1 

        pass

    def alguien_se_cuela(self, cliente: Cliente, posicion: int):
        # Completar
        
        if self.largo == 0:
            self.primer_nodo = cliente
            self.ultimo_nodo = cliente

        elif posicion == 0:
            self.primer_nodo.siguiente = cliente
            self.primer_nodo = cliente

        elif posicion >= self.largo:
            self.ultimo_nodo.siguiente = cliente
            self.ultimo_nodo = cliente

        elif (posicion > 0) and (posicion < self.largo):
            
            # Contendidos Listas Ligadas Ejemplo
            for _ in range(posicion - 1):
                if cliente is not None:
                    self.primer_nodo = self.primer_nodo.siguiente

            if self.primer_nodo is not None:

                cliente.siguiente = self.primer_nodo.siguiente
                self.primer_nodo.siguiente = cliente

                if cliente.siguiente is None:
                    self.ultimo_nodo = cliente
            
        pass
    
    def cliente_atendido(self):
        # Completar
        if self.largo > 1:
            lo_que_retorna = self.primer_nodo
            if self.primer_nodo is not None:
                self.primer_nodo = self.primer_nodo.siguiente

        elif self.largo == 1:
            lo_que_retorna = self.primer_nodo
            self.primer_nodo = None

        return lo_que_retorna
        
    def __str__(self):
        # Completar
        

        # Contenidos listas ligadas Ejemplo
        string_vacio = ""
        nodo_actual = self.primer_nodo

        while nodo_actual is not None:
            string_vacio = f"{string_vacio}{nodo_actual.nombre} → "
            nodo_actual = nodo_actual.siguiente

        return string_vacio
        
        pass


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)