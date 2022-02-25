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
    def añandirFrente(self, dato):
        self.head = nodo(dato=dato, direccionMemoriaDerecha=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def añadirFinal(self, dato):
        if not self.head:
            self.head = nodo(dato=dato)
            return
        nodoActual = self.head
        while nodoActual.direccionMemoriaDerecha:
            nodoActual = nodoActual.direccionMemoriaDerecha
        nodoActual.direccionMemoriaDerecha = nodo(dato=dato)
    
    # Método para eleminar nodos
    def borrarNodo(self, key):
        nodoActual = self.head
        prev = None
        while nodoActual and nodoActual.dato != key:
            prev = nodoActual
            nodoActual = nodoActual.direccionMemoriaDerecha
        if prev is None:
            self.head = nodoActual.direccionMemoriaDerecha
        elif nodoActual:
            prev.direccionMemoriaDerecha = nodoActual.direccionMemoriaDerecha
            nodoActual.direccionMemoriaDerecha = None

    # Método para imprimir la lista de nodos
    def imprimeLista( self ):
        nodo = self.head
        while nodo != None:
            print(nodo.dato, end =" -> ")
            nodo = nodo.direccionMemoriaDerecha


s = listaEncadenada()
s.añandirFrente(5)
s.añadirFinal(8) 
s.añandirFrente(9)
s.imprimeLista() 