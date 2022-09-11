"""
Integrantes:
David Arnoldo Hernández Gómez
Geovany Mauricio Alvarez Velasquez
"""

def valuser(user):
    length = len(user)
    if length < 6:
        print("El nombre de usuario tiene que tener como minimo 6.")
    elif length > 12: 
        print("El nombre de usuario tiene que tener como maximo 12 caracteres.")
    else:
        if user.isalnum():
            print("Nombre de usuario valido!")
        else:
            print("El nombre de usuario no puede contener caracteres especiales.")

def check_space(string): 
    count = 0
    for i in range(0, len(string)): 
        if string[i] == " ": 
            count += 1
    return count 

def valpas(password):
    length = len(password)
    if length <8:
        print("La contraseña escrita no es lo suficientemente segura.")
    elif check_space(password) != 0:
        print("La contraseña escrita no es lo suficientemente segura.")
    else:
        print("Contraseña valida!")