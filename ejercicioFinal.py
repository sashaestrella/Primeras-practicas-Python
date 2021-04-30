import os #cuenta con funciones para manejar archivos

#va en mayusculas porque es una constante
CARPETA = "contactos/"
EXTENSION = ".txt"

class Contacto:
    def __init__(self, nombre,apellido,email,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

#creo agenda de contactos en archivo
def app():

    crearDirectorio()
    mostrarMenu()

    preguntar = True
    while preguntar:
        opcion = input("Selecciona una opcion: \n")
        opcion = int(opcion)

        if opcion == 1:
            agregarContacto()
            preguntar = False
        elif opcion == 2:
            preguntar = False
        elif opcion == 3:
            preguntar = False
        elif opcion == 4:
            preguntar = False
        elif opcion == 5:
            preguntar = False
        else:
            print("Opción no válida, intente de nuevo por favor.")


def crearDirectorio():
    #si esta carpeta no existe entonces crear la carpeta
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
    

def mostrarMenu():
    print("Seleccione del menú lo que desea hacer")
    print("1) Agregar nuevo contacto")
    print("2) Editar contacto")
    print("3) Ver contactos")
    print("4) Buscar contacto")
    print("5) Eliminar contacto")

def agregarContacto():
    print("Escriba los datos del contacto que desea agregar.")
    nombre = input("Nombre:\n")

    existe = os.path.isfile(CARPETA+nombre+EXTENSION)
    if not existe:
        with open(CARPETA+nombre+EXTENSION,"w") as archivo:
            apellido = input("Apellido:\n")
            email = input("Email:\n")
            telefono = input("Telefono:\n")

            contacto = Contacto(nombre,apellido,email,telefono)

            archivo.write("Nombre: "+contacto.nombre+"\n")
            archivo.write("Apellido: "+contacto.apellido+"\n")
            archivo.write("Email: "+contacto.email+"\n")
            archivo.write("Teléfono: "+contacto.telefono+"\n")

            print("Contacto creado correctamente.\n\n")
    else:
        print("El contacto ya se encuentra creado.")
    app()

app()