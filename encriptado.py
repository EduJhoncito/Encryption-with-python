def encriptar(texto):
    textoFinal= " "
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal
def desencriptar(texto):
    textoFinal= " "
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto=(archivo.read())# con esto leemos el archivo que creamos
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, "w") #a = apend, w=write
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se encripto correctamente!!!")

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto=(archivo.read())# con esto leemos el archivo que creamos
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, "w") #a = apend, w=write
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se desencripto correctamente!!!")

respuestaEoD=input('Presione "E" para encriptar, o "D" para desencriptar: ')
rutaArchivo=input('Ingrese la ruta del archivo: ')

if respuestaEoD == "E":
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)
