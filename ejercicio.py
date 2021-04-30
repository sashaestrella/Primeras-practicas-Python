playlist = {}
playlist["canciones"] = [] #lista vacia

#funcion principal
def app():
    agregarPlaylist = True 
    while agregarPlaylist:
        nombrePlaylist = input("Como desea nombrar a la playlist?: ")
        if nombrePlaylist:
            playlist["nombre"] = nombrePlaylist
            agregarPlaylist = False
            agregarCanciones()

    #print(playlist["nombre"])


def agregarCanciones():
    agregarCancion = True

    while agregarCancion:
        nombrePlaylist = playlist["nombre"]
        pregunta = f"Agrega canciones a la playlist {nombrePlaylist}\r\n"
        pregunta += "Escribe 'N' para dejar de agregar.\r\n"
        respuesta = input(pregunta)

        if respuesta == "N":
            #dejar de agregar canciones
            print("finalizando....")
            agregarCancion = False
            mostrarResumen()
        else:
            playlist["canciones"].append(respuesta)

def mostrarResumen():
    print("Canciones:\n")
    for cancion in playlist["canciones"]:
        print(cancion)
            
        
app()