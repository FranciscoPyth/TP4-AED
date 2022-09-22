# Modulo principal para TP4... Exitos!!
from datetime import date
import os.path


# Parte colo, consigna 5 y 7
# --------------------------------------------------------------------------------
# 5- Buscar proyecto actualizado...

def validar_entre(inf, sup, mensaje):
    # En el caso que quiera ingresar un numero unicamente, coloco el int...
    opcion = input(mensaje)

    # En esta parte pensaba hacer la verificación también de si coloca por error una letra, para que no se rompa el
    # programa, es decir, esta funcion buscar que valide
    # tod tipo de caracter para que no provoque error en pantalla

    while opcion < inf and (opcion > sup):
        print("Opcion incorrecta! Vuelva a intentar...")
        opcion = input(mensaje)

    return opcion


def buscar_proyecto(vec, x):
    n = len(vec)
    for i in range(n):
        if vec[i] == x:
            print("Proyecto encontrado!")
            # En este punto mostramos el proyecto al usuario, para que pueda verificar qué es lo que contiene...

            print("Desea realizar algfuna modificación en su proyecto? ")
            print("1. Si\n" "2. No")

            opcion = validar_entre(1, 2, "Ingrese la opcion elegida: ")
            if opcion == 1:
                url = input("A continuación ingrese el URL nuevo porfavor: ")
                vec[i] = url

                # Aquí mismo realizamos el cambio de fechas...
                vec[i] = date.today()

                # También en este punto podríamos mostrarle el proyecto al usuario

            else:
                # Mostramos el proyecto sin haber sido actualizado...
                pass


# --------------------------------------------------------------------------------------------------------------------
# 7- Mostrar archivo...
# Aclaracion: Es independiente del programa principal, ya que debo mostrar los datos del archivo en forma de tabla...

def mostrar_archivo():
    m = open("proyectos.zip", "rb")
    if not os.path.exists("proyectos.zip"):
        print("Archivo Inexistente...")
        return

    # Para mostrar el archivo como matriz, pensaba en generarla y luego cargarle los datos...
    # Contamos la cantidad de filas de nuestro archivo
    # m = len(m)

    # Contamos cantidad de columnas de nuestro archivo
    # n = len(m[0])

    # Generamos la matriz para luego mostrar
    # mat = [[None] * m for f in range(n)]


def principal():
    pass


if __name__ == '__main__':
    principal()
