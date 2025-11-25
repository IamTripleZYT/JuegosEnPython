# aqui esta el codigo
# este programa tendra piedra papel o tijera, adivina el numero, una calculadora y un juego para sumar numeros.
# recuerda que \n se utiliza para hacer un salto de linea
import math
import random
# aqui estan las funciones de los juegos:
def jugarPPTSV():
    while True:
        opcionesppt = ["piedra", "papel", "tijera"]
        opcionJm = input("Piedra, papel o tijera?: ")
        opcionJ = opcionJm.lower()
        opcionBm = random.choice(opcionesppt)
        opcionB = opcionBm.lower()

        while opcionJ not in opcionesppt:
            print("Escriba una opcion valida")
            opcionJ = str(input("Piedra, papel o tijera? "))

        if opcionJ == opcionB:
            print(f"tu: {opcionJ}")
            print(f"Bot: {opcionB}")
            print("\nEmpate!")

        elif opcionJ == "papel" and opcionB == "tijera" or opcionJ == "piedra" and opcionB == "papel" or opcionJ == "tijera" and opcionB == "piedra":
            print(f"tu: {opcionJ}")
            print(f"Bot: {opcionB}")
            print("Perdiste, intentalo de nuevo")
        elif opcionB == "papel" and opcionJ == "tijera" or opcionB == "piedra" and opcionJ == "papel" or opcionB == "tijera" and opcionJ == "piedra":
            print(f"tu: {opcionJ}")
            print(f"Bot: {opcionB}")
            print("Ganaste! \n\n\n\n")
            break



def jugarPPTCV():
    vidas = 5
    while True:
        opcionesppt = ["piedra", "papel", "tijera"]
        opcionJm = input("Piedra, papel o tijera?: ")
        opcionJ = opcionJm.lower()
        opcionBm = random.choice(opcionesppt)
        opcionB = opcionBm.lower()

        while opcionJ not in opcionesppt:
            print("Escriba una opcion valida")
            opcionJ = str(input("Piedra, papel o tijera? "))

        if opcionJ == opcionB:
            vidas -= 1
            print(f"tu: {opcionJ}")
            print(f"Bot: {opcionB}")
            print("\nEmpate!")

        elif opcionJ == "papel" and opcionB == "tijera" or opcionJ == "piedra" and opcionB == "papel" or opcionJ == "tijera" and opcionB == "piedra":
            vidas -= 1
            print(f"tu: {opcionJ}")
            print(f"Bot: {opcionB}")
            print("Perdiste, intentalo de nuevo")
        elif opcionB == "papel" and opcionJ == "tijera" or opcionB == "piedra" and opcionJ == "papel" or opcionB == "tijera" and opcionJ == "piedra":
                print(f"tu: {opcionJ}")
                print(f"Bot: {opcionB}")
                print(f"Ganaste con {vidas} vidas \n\n\n\n")
                break



def jugarPPT():
    print("Quiere jugar con vidas o sin vidas?")
    modo = str(input("cv/sv "))
    while modo != "cv" or modo != "sv":
        print("Escoja un modo valido")
        modo = input("cv/sv ")
    if modo == "cv":
        jugarPPTCV()
    elif modo == "sv":
        jugarPPTSV()



def Adivina_num():
    numeroS = random.randint(1,100)
    intentos = 1
    print("Quiere jugar el modo facil, medio, dificil o personalizado?")
    modo = input("(f/m/d/p): ")
    if modo == "f" or modo == "facil":
        while True:
            eleccion = int(input("Adivine el numero del 1 al 100: "))

            if eleccion == numeroS:
                print(f"Ganaste en {intentos} intentos \n\n\n\n")
                break
            elif eleccion > numeroS:
                print("Mas bajo")
                intentos += 1
            elif eleccion < numeroS:
                print("mas alto")
                intentos += 1
    elif modo == "m" or modo == "medio":
        numeroS = random.randint(1, 250)
        while True:
            eleccion = int(input("Adivine el numero del 1 al 250: "))

            if eleccion == numeroS:
                print(f"Ganaste en {intentos} intentos \n\n\n\n")
                break
            elif eleccion > numeroS:
                print("Mas bajo")
                intentos += 1
            elif eleccion < numeroS:
                print("mas alto")
                intentos += 1
    elif modo == "d" or modo == "dificil":
        numeroS = random.randint(1, 500)
        while True:
            eleccion = int(input("Adivine el numero del 1 al 500: "))

            if eleccion == numeroS:
                print(f"Ganaste en {intentos} intentos \n\n\n\n")
                break
            elif eleccion > numeroS:
                print("Mas bajo")
                intentos += 1
            elif eleccion < numeroS:
                print("mas alto")
                intentos += 1
    elif modo == "p" or modo == "personalizado":

        rango = int(input("Ingrese el número máximo del rango: "))
        numeroS = random.randint(1,rango)
        if rango <= 0:
            print("Introduzca un número válido mayor que 0")
            return
        while True:
            eleccion = int(input(f"Adivine el numero del 1 al {rango}: "))

            if eleccion == numeroS:
                print(f"Ganaste en {intentos} intentos \n\n\n\n")
                break
            elif eleccion > numeroS:
                print("Mas bajo")
                intentos += 1
            elif eleccion < numeroS:
                print("mas alto")
                intentos += 1



def sumar(a,b):
    resultado = a + b
    print(f"{a} mas {b} es {resultado}\n")
def restar(a,b):
    resultado = a - b
    print(f"{a} menos {b} es {resultado}\n")
def multiplicar(a,b):
    resultado = a * b
    print(f"{a} por {b} es {resultado}\n")
def dividir(a,b):
    resultado = a / b
    print(f"{a} entre {b} es {resultado}\n")
def potencia(a,b):
    resultado = pow(a,b)
    print(f"{a} a la potencia de {b} es {resultado}\n")
def raiz(a):
    resultado = math.sqrt(a)
    print(f"la raiz de {a} es {resultado}\n")



def calculadora():
    print("Calculadora")
    print("Escriba el numero de la operacion que desea realizar ")
    while True:
        operacion = input("1. sumar \n2. restar \n3. multiplicar \n4. dividir \n5. potencia \n6. raiz cuadrada \nq para salir ")
        if operacion == "1":
            a = int(input("Escriba el primer numero: "))
            b = int(input("Escriba el segundo numero: "))
            sumar(a,b)

        elif operacion == "2":
            a = int(input("Escriba el primer numero: "))
            b = int(input("Escriba el segundo numero: "))
            restar(a,b)

        elif operacion == "3":
            a = int(input("Escriba el primer numero: "))
            b = int(input("Escriba el segundo numero: "))
            multiplicar(a, b)

        elif operacion == "4":
            a = int(input("Escriba el primer numero: "))
            b = int(input("Escriba el segundo numero: "))
            dividir(a,b)

        elif operacion == "5":
            a = int(input("Escriba el primer numero: "))
            b = int(input("Escriba el segundo numero: "))
            potencia(a,b)

        elif operacion == "6":
            a = int(input("Escriba el numero: "))
            raiz(a)

        elif operacion == "q":
            print("Saliendo.... \n\n\n\n")
            break
        else:
            print("Operacion invalida, intentelo denuevo")



def juego_sumar():
    intentos = 1
    while True:
        num_a = random.randint(1,1000)
        num_b = random.randint(1,1000)
        resultadoR = num_a + num_b
        resultadoJ = input(f"Cuanto es {num_a} mas {num_b}? ")
        while resultadoJ != resultadoR:
            print("Siga intentando ")
            intentos += 1
            resultadoJ = int(input(f"cuanto es {num_a} mas {num_b} "))
        print("Adivinaste! ")
        print(f"Lo hiciste en {intentos} intentos")
        break


# Este es el juego principal
def Juego():
    print("Juegos simples")
    while True:
        juegoAjugar = int(input("Escriba el numero del juego que quiere probar: \n"
                                "1. Adivina el numero \n"
                                "2. Calculadora \n"
                                "3. Suma los dos numeros \n"
                                "4. Piedra, papel o tijera \n"
                                "5. Salir "))
        if juegoAjugar == 1:
            Adivina_num()
        elif juegoAjugar == 2:
            calculadora()
        elif juegoAjugar == 3:
            juego_sumar()
        elif juegoAjugar == 4:
            jugarPPT()
        elif juegoAjugar == 5:
            print("Gracias por jugar!")
            break
Juego()
