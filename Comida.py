class Comida:
    def __init__(self, nombre):
        self.nombre=nombre
Plato1 = Comida('Pollo en Cebollado')
Plato2 = Comida('Sapo de Res')

class Maria(Comida):
    pass
    def comidas():
        return 'Maria van a comprar el plato de comida de {}'.format(Plato1.nombre)

class Laura(Comida):
    pass
    def comidas():
        return 'Laura van a comprar el plato de comida de {}'.format(Plato2.nombre)
compra1 = Maria
print(compra1.comidas())        
compra2 = Laura
print(compra2.comidas())