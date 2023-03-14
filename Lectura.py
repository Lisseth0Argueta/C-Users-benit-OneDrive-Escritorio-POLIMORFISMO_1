class Leerlibros:
    def __init__(self, nombre):
        self.nombre=nombre
lecctura1 = Leerlibros("Cien años de soledad")
lecctura2 = Leerlibros("El dinero Maldito")

class Camila(Leerlibros):
    pass
    def estanLeido():
        return 'Camila estan leido el libro {}'.format(lecctura1.nombre)

class Veronica(Leerlibros):
    pass
    def estanLeido():
        return 'Veronica estan leido el libro {}'.format(lecctura2.nombre)


Libro1 = Camila
Libro2 = Veronica
print(Libro1.estanLeido())
print(Libro2.estanLeido())