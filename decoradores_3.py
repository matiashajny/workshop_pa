#Crea un decorador @authorize que solo permita ejecutar una función si un parámetro user
#tiene el atributo is_admin=True. Si no, debe imprimir “Acceso denegado”. Prueba el 

def authorize(func):
    def wrapper(user, *args, **kwargs):
        if getattr(user, "is_admin", False):
            return func(user, *args, **kwargs)
        else:
            print("Acceso denegado")
    return wrapper

class Usuario:
    def __init__(self, nombre, is_admin):
        self.nombre = nombre
        self.is_admin = is_admin

@authorize
def acceso_restringido(user):
    print(f"Acceso concedido a {user.nombre}")
