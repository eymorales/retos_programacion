# El carácter infiltrado

# Crea una función que reciba dos cadenas de texto casi iguales,
# a excepción de uno o varios carácteres.
# La función debe encontrarlos y retornarlos en formato lista/array.
# - Ambas cadenas de texto deben ser iguales en longitud
# - Las cadenas de texto son iguales elemento a elemento.
# - No se pueden utilizar operaciones propias del lenguaje que
#   lo resuelvan directamente.

# Ejemplos:
# - Me llamo Sergio / Me llemo Serguo -> ["e", "u"]
# - Me llamo.Sergio / Me llamo sergio -> [" ", "s"]


cad1 = "Me llamo Sergio"
cad2 = "ME llemo Serguo"

def EncontrarCaracter (cad1: str, cad2: str):
    caracteres = []

    for i in range(len(cad1)):
        if cad1[i] != cad2[i]:
            caracteres.append(cad2[i])
    return caracteres
        
print(EncontrarCaracter(cad1, cad2))

