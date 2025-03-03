# Archivo de prueba en python para Code Climate
import os
import sys

# Variable no alcanzable ni utilizada
x = 10

def bad_function():
    print("Esta función no es muy correcta")
    
    for i in range(10):
        print("No utiliza i") 
    return 42

# Código no estructurado correctamente
if __name__ == "__main__":
    bad_function()
    print("Fin del script")
