import os
import qrcode
from PIL import Image


#-------------------------------DEFINICIÓN DEL QRGenerator--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Qr():
    Cadena = input("Introduzca el texto para el codigo Qr: ")                                #se ingresa el link que se abrira cuando se escanee el qr
    imagen = qrcode.make(Cadena)

    nombre_imagen = input("Introduzca el nombre que tendra el archivo imagen: ") + '.png'    #se ingresa el nombre con el que se guardara el archivo
    path = 'Archivos_Qr/' + nombre_imagen
    with open(path,'wb') as archivo_imagen:
        imagen.save(archivo_imagen)
        

    return 0
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------DEFINICIÓN DEL MAIN--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    if os.path.isdir('Archivos_Qr'):                                                          #pregunto si ya hay un directorio para guardar los Qr
        pass

    else:
        os.mkdir('Archivos_Qr')                                                               #En el caso contrario creo dicho directorio


    condition = True

    while condition:
        Qr()
        
        opcion = input('Se desea crear mas codigos Qr Y/N: ')

        if(opcion == 'Y'):
            condition = True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        if(opcion == 'N'):
            condition = False

        if(opcion != 'Y' and opcion != 'N'):
            condition = False    



    return 0
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
