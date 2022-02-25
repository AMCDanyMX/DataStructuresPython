class Node:  
    def __init__(self, dato):
        self.item = dato
        self.direccionMemoriaDerecha = None
        self.direccionMemoriaIzquierda = None
        
class ListaDobleLigada:  
    def __init__(self):
        self.nodo_inicial = None
        
    def insert_in_emptylist(self, dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Node(dato)
            self.nodo_inicial = nuevo_nodo
        else:
            print("Lista no esta vacia")   
            
    def pushFront(self, dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Node(dato)
            self.nodo_inicial = nuevo_nodo
            print("Nodo agregado")
            return
        nuevo_nodo = Node(dato)
        nuevo_nodo.direccionMemoriaDerecha = self.nodo_inicial
        self.nodo_inicial.direccionMemoriaIzquierda = nuevo_nodo
        self.nodo_inicial = nuevo_nodo
        
    def pushBack(self, dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Node(dato)
            self.nodo_inicial = nuevo_nodo
            return
        n = self.nodo_inicial
        while n.direccionMemoriaDerecha is not None:
            n = n.direccionMemoriaDerecha
        nuevo_nodo = Node(dato)
        n.direccionMemoriaDerecha = nuevo_nodo
        nuevo_nodo.direccionMemoriaIzquierda = n

    def popFront(self):
        if self.nodo_inicial is None:
            print("La lista no tiene elementos para borrar")
            return 
        if self.nodo_inicial.direccionMemoriaDerecha is None:
            self.nodo_inicial = None
            return
        self.nodo_inicial = self.nodo_inicial.direccionMemoriaDerecha
        self.start_prev = None

    def popBack(self):
        if self.nodo_inicial is None:
            print("La lista no tiene elementos para borrar")
            return 
        if self.nodo_inicial.direccionMemoriaDerecha is None:
            self.nodo_inicial = None
            return
        n = self.nodo_inicial
        while n.direccionMemoriaDerecha is not None:
            n = n.direccionMemoriaDerecha
        n.direccionMemoriaIzquierda.direccionMemoriaDerecha = None
        
    def imprimirLista(self):
        if self.nodo_inicial is None:
            print("La lista no tiene elementos/nodos")
            return
        else:
            n = self.nodo_inicial
            while n is not None:
                print(n.item , end =" <--> ")
                n = n.direccionMemoriaDerecha
        
nuevaListaDoble = ListaDobleLigada() 
nuevaListaDoble.insert_in_emptylist(33)
nuevaListaDoble.pushFront(24)
nuevaListaDoble.pushBack(26)
nuevaListaDoble.imprimirLista()

