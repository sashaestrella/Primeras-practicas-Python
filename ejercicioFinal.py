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
            editarCotacto()
            preguntar = False
        elif opcion == 3:
            verContactos()
            preguntar = False
        elif opcion == 4:
            buscarContacto()
            preguntar = False
        elif opcion == 5:
            eliminarContacto()
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

def editarCotacto():
    print("Escribe el nombre del contacto a editar.\n")
    nombre = input("Nombre del contacto que desea editar:\n")

    existe = os.path.isfile(CARPETA+nombre+EXTENSION)
    if existe:
        with open(CARPETA+nombre+EXTENSION,"w") as archivo:
            nombreNuevo = input("Nuevo nombre:\n")
            apellido = input("Nuevo apellido:\n")
            email = input("Nuevo email:\n")
            telefono = input("Nuevo telefono:\n")

            contacto = Contacto(nombreNuevo,apellido,email,telefono)
            archivo.write("Nombre: "+contacto.nombre+"\n")
            archivo.write("Apellido: "+contacto.apellido+"\n")
            archivo.write("Email: "+contacto.email+"\n")
            archivo.write("Teléfono: "+contacto.telefono+"\n")

            #renombrar el archivo con el nuevo nombre
        os.rename(CARPETA+nombre+EXTENSION, CARPETA+nombreNuevo+EXTENSION)
        print("Contacto editado correctamente.")
    else:
        print("Ese contacto no existe.")
        app()

def verContactos():
    archivos = os.listdir(CARPETA)

    #recorro el iterador pero solamente si el archivo es .txt
    archivosTxt = [i for i in archivos if i.endswith(EXTENSION)]
    print("\nContactos:")
    for archivo in archivosTxt:
        with open(CARPETA+archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print("\n")
    app()

def buscarContacto():
    nombre = input("Diga el nombre del contacto que desea buscar: ")

    try:
        with open(CARPETA+nombre+EXTENSION) as contacto:
            for linea in contacto:
                print(linea.rstrip())
    except IOError:
        print("El archivo no existe")
        print(IOError)
    app()

def eliminarContacto():
    nombre = input("Diga el nombre del contacto que desea eliminar: ")

    try: 
        os.remove(CARPETA+nombre+EXTENSION)
        print("Contacto eliminado correctamente.")
    except expresion as identifier:
        print("El contacto no existe.")
    app()

app()