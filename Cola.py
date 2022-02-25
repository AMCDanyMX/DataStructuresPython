class Cola:
    "" "Cola de simulación" ""
    def __init__(self):
        self.items = []

    def enCola(self, items):
        self.items.append(items)

    def desencolar(self):
        self.items.pop(0)

    def clear(self):
        del self.items

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)

print("Crear cola")
Cola =  Cola()
Cola.print()
print("Insertar elementos en la cola")
Cola.enCola(4)
Cola.print()
print("Eliminar elemento de la cola")
Cola.desencolar()
Cola.print()
print("Determinar si la cola está vacía")
print(Cola.is_empty())
print("Devuelve el número de elementos en la cola")
print(Cola.size())
Cola.print()
#print("Cola vacía")
#print(Cola.clear())
