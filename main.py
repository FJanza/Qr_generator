import qrcode
from PIL import Image


#-------------------------------DEFINICIÓN DEL QRGenerator--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Qr():
    Cadena = input("Introduzca el texto para el codigo Qr: ")     #se ingresa el link que se abrira cuando se escanee el qr
    imagen = qrcode.make(Cadena)

    nombre_imagen = input("Introduzca el nombre que tendra el archivo imagen: ")
    archivo_imagen = open(nombre_imagen,'wb')
    imagen.save(archivo_imagen)
    archivo_imagen.close()

    return 0
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------DEFINICIÓN DEL MAIN--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    



    return 0
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
