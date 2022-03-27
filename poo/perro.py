class Perro:
    #constructor
    def __init__(self, n, r, c):
        self.tamaño = None
        self.edad = 0
        self.color = c
        self.raza = r
        self.nombre = n
    
    #métodos
    def ladrar(self):
        print("{} está ladrando".format(self.nombre))

    def check_hambre(self,hambre):
        if hambre:
            self.comer()
        else:
            print(f"{self.nombre} no está hambriento")

    def comer(self):
        print("{} está comiendo".format(self.nombre))

    def jugar(self):
        print("{} está jugando".format(self.nombre))

    #setter // getter
    def cambiar_nombre(self,nombre):
        self.nombre = nombre
        print("El perro ahora se llama {}".format(nombre))

    def set_edad(self,edad):
        self.edad = edad
        print("{} ahora tiene {} años".format(self.nombre,self.edad))
    
    def cumpleaños(self):
        self.edad += 1
        print("{} ahora tiene {} años".format(self.nombre,self.edad))




# instanciar un objeto
tommy = Perro("Tommy","Dalmata","Blanco y negro")
print(tommy.nombre)
tommy.comer()
tommy.cumpleaños()
tommy.check_hambre(True)


rex= Perro("Rex","Pitbull","Marron")
rex.jugar()
rex.set_edad(5)
rex.check_hambre(False)