'''Programar en Python un generador de códigos qr personalizados (tamaño y color definidos por el usuario), el qr debe enlazar a la url de Python'''

'''Advertencia, la personalización de los colores del Código QR a generar solo será posible si el usuario tiene instalado el módulo "Pillow"'''

# Primero, se importa el módulo "qrcode" que agrega todas las características utilizadas para generar Códigos QR
import qrcode

# Según los establecido por el enunciado, el usuario debe ser capaz de personalizar el tamaño del código generado, al igual que sus respectivos colores, por ello, primero se crearán las variables que almacenaran dichos datos y se permitirá al usuario ingresar sus respectivos valores utilizando la función "input(...)". 
print("A continuación se va a crear un Código QR que direccionará a la página de Python, por favor...")
tamano = int(input("Ingrese el tamaño de las cajas (los cuadrados) del Código QR en píxeles: "))
color_codigo = input("Ingrese el color en inglés del Código QR:  ")
color_fondo = input("Ingrese el color en inglés del fondo del Código QR:  ")

# Se creará el Código QR en forma de un objeto utilizando el método propio del módulo "qrcode", "QRCode"; el objeto poseerá 4 características:
    #- "error_correction" que sirve para corregir errores que se detecten en la creación, a este se le almacena el valor "qrcode.constants.ERROR_CORRECT_L", que sirve para establecer que se debe corregir un 7% de los errores que se encuentren en el Código QR generado
    #- "box_size" Establece cual es el tamaño de las cajas (cada cuadrado que en conjunto generan el código) del código a generar en pixeles, su valor es aquel que haya sido almacenado en la variable "tamano" (el valor fue dado por el usuario)
    #- "border" que es el tamaño del borde que tendrá el Código QR con el resto de la imagen, el tamaño esta dado en cajas; se establecerá un tamaño de 2 cajas
# El objeto generado se almacenará en la variable generada "Codigo_QR"
Codigo_QR = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = tamano,
                    border = 2
                    )

# Para agregar que información almacenara el Código QR generado, se utilizara el método "add_data", el cual almacenara la dirección a la página principal de Python "https://www.python.org/", en forma de texto.
Codigo_QR.add_data("https://www.python.org/")

# Se aplica al Código Qr 
Codigo_QR.make(fit = True)

# Ahora, se convertirá el objeto presente en "Codigo_QR" a una imagen, para ello se usara el método "make_image" al cual se les alterará los atributos "fill_color" que afecta al color de las cajas negras y a "back_color" que afecta al color de las cajas blancas; a estos atributos se les almacenará el valor dado por el usuario.

# Hay que denotar, que las propiedades de "make_image", solo se ejecutan cuando el usuario tiene instalado también el módulo "Pillow", debido a que "make_image" llama a ejecutar funciones de dicho modulo. Si no se tiene instalado, los colores no cambiaran. La imagen generada, se almacena en la variable creada "img"
img =  Codigo_QR.make_image(fill_color = color_codigo,
                            back_color = color_fondo)

# Se almacenará la imagen creada utilizando el método "save(...)", donde, dentro del texto entre paréntesis, se almacena la dirección en la cual se debe almacenar la imagen generada y/o el nombre y extensión de la imagen; en este caso, al no presentar dirección, la imagen que contiene el Código QR se almacenará en la misma carpeta en la cual se ubique el archivo de "Ejercicio 2.py" y el nombre de la imagen será "Codigo QR" y tendrá la extensión ".png"
img.save('Codigo QR.png')

# Para finalizar, se avisa al usuario que se ha generado el Código QR y cuál es su ubicación, utilizando la función "print(...)"
print("El código se generó exitosamente, el Código QR generado se ubica en la misma carpeta que este archivo")


