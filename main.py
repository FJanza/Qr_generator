import os
import qrcode
from PIL import Image


def QR():
    """Definición del QRGenerator."""

    cadena = input("Introduzca el link para el codigo QR: ")
    imagen = qrcode.make(cadena)

    nombre_imagen = input("Introduzca el nombre que tendra el archivo imagen: ") + '.png'
    path = "Archivos_QR/" + nombre_imagen

    os.makedirs(os.path.dirname(path))  # crea el directorio si no existe

    with open(path, 'wb') as archivo_imagen:
        imagen.save(archivo_imagen)


def main():
    """Definición del main."""

    repetir = True

    while repetir:
        QR()
        opcion = input('Se desea crear mas codigos Qr Y/N: ')
        repetir = True if opcion == 'Y' else False


if __name__ == '__main__':
    main()
