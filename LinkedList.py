# NODOS
class nodo:
    def __init__(self, dato = None, direccionMemoriaDerecha = None):
        self.dato = dato
        self.direccionMemoriaDerecha = direccionMemoriaDerecha

# Creamos la clase listaEncadenada
class listaEncadenada: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, dato):
        self.head = nodo(dato=dato, direccionMemoriaDerecha=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, dato):
        if not self.head:
            self.head = nodo(dato=dato)
            return
        curr = self.head
        while curr.direccionMemoriaDerecha:
            curr = curr.direccionMemoriaDerecha
        curr.direccionMemoriaDerecha = nodo(dato=dato)
    
    # Método para eleminar nodos
    def delete_nodo(self, key):
        curr = self.head
        prev = None
        while curr and curr.dato != key:
            prev = curr
            curr = curr.direccionMemoriaDerecha
        if prev is None:
            self.head = curr.direccionMemoriaDerecha
        elif curr:
            prev.direccionMemoriaDerecha = curr.direccionMemoriaDerecha
            curr.direccionMemoriaDerecha = None

    # Método para obtener el ultimo nodo
    def get_last_nodo(self):
        temp = self.head
        while(temp.direccionMemoriaDerecha is not None):
            temp = temp.direccionMemoriaDerecha
        return temp.dato

    # Método para imprimir la lista de nodos
    def print_list( self ):
        nodo = self.head
        while nodo != None:
            print(nodo.dato, end =" -> ")
            nodo = nodo.direccionMemoriaDerecha


s = listaEncadenada() # Instancia de la clase
s.add_at_front(5) # Agregamos un elemento al frente del nodo
s.add_at_end(8) # Agregamos un elemento al final del nodo
s.add_at_front(9) # Agregamos otro elemento al frente del nodo

s.print_list() # Imprimimos la lista de nodos