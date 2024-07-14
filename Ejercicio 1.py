''' Programar en Python un generador de contraseñas aleatorio.'''

# Primero se importan los módulos que implementan características especiales al código, en este caso se usaran los módulos
#     - "secrets", que es un módulo especializado en la creación de contraseñas
#     - "string", que es un módulo que sirve para trabajar mejor con caracteres
import secrets 
import string 

# Para crear un generador de contraseñas, primero hay que considerar que requisitos debería tener el generador para construir contraseñas. En este caso, se usarán los requisitos más básicos que debe tener una contraseña segura, que son:
#     1. La contraseña debe tener al menos 10 caracteres (en este caso, serán exactamente 10 caracteres)
#     2. La contraseña debe contener al menos una letra minúscula
#     3. La contraseña debe contener al menos una letra mayúscula
#     4. La contraseña debe contener al menos un numero
#     5. La estructura de la contraseña debe ser totalmente aleatoria
# Con esto establecido, se codificará un generador de contraseñas que cumpla con estas características

# Para crear el generador, primero se establecerán que caracteres estarán permitidos en la creación de las contraseñas, para ello, se crea la variable "Alfabeto", el cual almacenara 2 datos propios del módulo "string", el "string.ascii_letters", que almacena el abecedario tanto en letras mayúsculas como minúsculas, y "string.digits", que almacena los números del 0 al 9, y se agrega 2 veces para aumentar las probabilidades de que se la contraseña al menos posea un número. De esta forma, "Alfabeto" será utilizado para contener todos los caracteres que serán utilizados para construir contraseñas.
Alfabeto = string.ascii_letters + string.digits + string.digits

# Se crea el contador "i", el cual será utilizado para detener a la estructura "while...else" que le sigue.
i = 0

# Se usa la estructura "while...else" para hacer que se repita el proceso de construcción de la contraseña, hasta que la contraseña creada cumpla con los requisitos establecidos; donde el "while" repite el proceso y una vez el bucle es terminado, se ejecuta el código presente en "else".
# Para mantener el bucle, se establece que este seguirá mientras "i" no sea igual a 1.
while 1 != i:
    # En el primer ciclo, se crea la variable "contraseña", que almacenara la contraseña creada, por ello al inicio esta vacío. Pero, si la contraseña no cumple lo especificado, en el segundo ciclo se vacía la variable, eliminando la contraseña fallida, y se vuelve a iniciar el proceso; este procedimiento se mantendrá hasta que la contraseña sea adecuada.
    contasena = ''

    # Se crea una estructura "for...in", donde se usara un contador "j" el cual comenzara valiendo 0 y en cada ciclo, aumentara su valor en 1, hasta llegar a 9, haciendo que se repita el bucle 10 veces, tal y como se establece en "range(10)".

    # En cada ciclo del "for...in" se concatena a la variable "contraseña" el carácter resultante de "secrets.choice(Alfabeto)"; en este se aplica la función "choice(...)", una función propia del módulo "secrets", que toma un carácter aleatorio de la variable que tiene entre paréntesis (en este caso, de "Alfabeto") para que este pueda ser utilizado, en este caso, para concatenarlo en "contrasena". Este proceso se repetirá 10 veces, de tal forma que queda una contraseña de 10 caracteres puestos de forma aleatoria; cumpliendo así con el primer y el último requisito establecido al inicio, por lo cual, ahora hay que asegurarse de que se cumplan el segundo, el tercero y el cuarto.
    for j in range(10):
        contasena += secrets.choice(Alfabeto)
    
    # Se crea una estructura condicional "if", donde se establece que deben cumplirse 3 condiciones, que son:
    #- "any(k.islower() for k in contraseña)" Se utiliza la función "any(...)" que, si dentro de una serie de expresiones booleanas, una sola al menos es "true", presenta un "true" como resultado, sino, presenta "false"; en este caso, se ejecuta un "for...in" de forma resumida, donde, se usara el contador "k", para almacenar un carácter de "contrasena" y de allí se comprobara si el carácter es una letra minúscula utilizando el método "islower()". De esta forma, si al menos un solo carácter es una letra minúscula, "any(k.islower() for k in contasena)" será "true".

    #- "any(k.isupper() for k in contasena)" Se realiza el mismo procedimiento que en el caso anterior, solo que en este caso, se comprueba si al menos un carácter es una letra mayúscula, utilizando el método "isupper()", y si al menos un carácter lo es "any(k.isupper for k in contasena)" será "true"

    #- "any(k.isdigit() for k in contasena)" Se realiza el mismo procedimiento que en el caso anterior, solo que en este caso, se comprueba si al menos un carácter es un número, utilizando el método "isdigit()", y si al menos un carácter lo es "any(k.isdigit() for k in contasena)" será "true".

    if any(k.islower() for k in contasena) and any(k.isupper() for k in contasena) and any(k.isdigit() for k in contasena):
        #  si las 3 condiciones se cumplen, se le asignará al contador del "while", "i", un valor de 1, lo que romperá el bucle
         i=1
#     De esta forma se cumplen los 3 requisitos faltantes

#     Si tras la generación de la contraseña, esta no cumple con las 3 condiciones del "if", se repetirá el bucle, así hasta que la contraseña sea adecuada y se rompa el bucle con el comando "i=1"

# Una vez se rompe el bucle, se ejecuta el código del "else", que es mostrar en pantalla la contraseña generada, usando la función "print()"
else:
    print("Se ha generado la contraseña: " + contasena) 


