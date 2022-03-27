class User:
    def __init__(self):
        self.email = input("Introduzca su email: ")
        self.__password = input("Introduzca su contraseña: ")
        self.permissions = ['edit','create','update']
        self.username = None
    

    def setear_username(self):
        self.username = input("Introduzca el username que desea tener: ")
        print("Username cambiado exitosamente a : {}".format(self.username))


class UserPro(User):
    def __init__(self):
        super().__init__()
        self.permissions += ['delete','download']

    def pay_suscription(self,monto):
        print("Usted ha pagado exitosamente la suscripcion ({})".format(monto))


class UserManager:
    def create_user(self,suscripcion):
        if suscripcion:
            user = UserPro()
        else:
            user = User()

        print("Se ha creado exitosamente su usuario. Sus permisos son: {}".format(user.permissions))


UserManager().create_user(False)

