def app():
    archivo = open("archivo.txt", "w")

    for i in range(1,20):
        archivo.write("Esta es la linea "+str(i)+"\r")

    archivo.close()

app()