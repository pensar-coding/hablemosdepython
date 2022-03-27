class Animal:
    def __init__(self):
        self.edad = None
        self.especie = None
        self.pelaje = None

    def comer(self):
        print("El animal está comiendo")

    def reproducirse(self):
        print("El animal se está reproduciendo")

    def set_especie(self,e):
        self.especie = e


class Perro(Animal):
    def __init__(self):
        super().__init__()
        self.tamaño = None
        self.raza = None
        self.nombre = None
        self.especie = self.set_especie("Perro")

    def ladrar(self):
        print("{} está ladrando".format(self.nombre))

    def jugar(self):
        print("{} está jugando".format(self.nombre))


tommy = Perro()
tommy.set_especie("Perro")
print(tommy.especie)