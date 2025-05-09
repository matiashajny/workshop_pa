#corregir el codigo

def decorator(func):
    print("Decorating...")
    
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = func(*args, **kwargs)
        print("Después de la función")
        return resultado
    
    return wrapper

@decorator
def greet():
    print("Hi!")

greet()
