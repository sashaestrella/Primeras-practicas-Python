#variables 
texto = "Hola"
nombre = "Sasha"

print(f"{texto} {nombre}")
print(texto + " " + nombre)

#entrada
paginaWeb = input("Cual es tu pagina web?: ")
print(paginaWeb)

#condiciones
"""
altura = int(input("Cual es tu altura?: "))
if altura >= 180:
    print("Eres una persona alta")
else:
    print("Eres una persona bajita")
"""
#funciones (con el def decimos que es una funcion)
def mostrarAltura():
    altura = int(input("Cual es tu altura?: "))
    if altura >= 180:
        print("Eres una persona alta")
    else:
        print("Eres una persona bajita")
    
    return 0

mostrarAltura()

#listas (el bucle for itera segun la cantidad de elementos que contenga la lista)
animales = ["julian","jax","heavenly","hazel"]
print(animales[0])

for animal in animales:
    print("El animal es:"+animal)

#creando diccionario simple 
cancion = {
    "artista":"Pearl Jam",
    "cancion":"Even Flow",
    "lanzamiento":1990
}

#crear diccionario vacio
#cancion = {}

print(cancion)
print(f"El artista es {cancion['artista']}")

#agregar nuevo valor al diccionario 
cancion["playlist"] = "Rock grunge"
print(cancion)

#reemplazar valor del diccionario (si no existe lo agrega, sino lo cambia)
cancion["cancion"] = "Jeremy"
print(cancion)

#eliminar valor del diccionario
del cancion["lanzamiento"]
print(cancion)

print(cancion.get("consola", "No existe ese valor en dicho diccionario"))

for llave,valor in cancion.items():
    print(llave) #artista
    print(valor) #pearl jam

