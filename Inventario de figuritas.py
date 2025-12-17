import json

Figuras = {}


# ----------------------------------------
# Esta parte es para guardar en un archivo
# ----------------------------------------

def Guardar_figuras():
    with open("figuras.json", "w", encoding="utf-8") as archivo:
        json.dump(Figuras, archivo, indent=4, ensure_ascii=False)


def cargar_figuras():
    global Figuras
    try:
        with open("figuras.json", "r", encoding="utf-8") as archivo:
            Figuras = json.load(archivo)
    except FileNotFoundError:
        Figuras = {}


# -------------------------------------------------
# Esta parte son las funciones de el programa en si
# -------------------------------------------------

# nombre, precio, tipo, marca.
def agregar_figura(nombre, precio, tipo, marca):
    id = len(Figuras) + 1
    tipo = str(tipo)
    precio = float(precio)
    if id in Figuras:
        print("Ya tenemos esa figura\n\n\n")
    else:
        try:
            tipos = ["futbol", "heroe", "villano"]
            tipos = tipos
            int(precio)
            if tipo not in tipos:
                print("Tienes que escoger un tipo valido\n\n\n")
            else:
                Figuras[id] = {}
                Figuras[id]["nombre"] = nombre
                Figuras[id]["precio"] = round(float(precio), 2)
                Figuras[id]["tipo"] = tipo
                Figuras[id]["marca"] = marca
        except ValueError:
            print(f"{precio} no puede ser un precio\n\n\n")


def eliminar_figura(id):
    id = int(id)
    if id not in Figuras:
        print("Ese id no existe\n\n\n")
    else:
        print(f"{Figuras[id]["nombre"]} eliminado con exito\n\n\n")
        Figuras.pop(id)


def Mostrar_figuras():
    if len(Figuras) == 0:
        print("No hay figuras disponibles\n\n\n")
    else:
        for id, datos in Figuras.items():
            print(f"id: {id}(\n"
                  f"        Nombre: {datos['nombre']}\n"
                  f"        Precio: {datos['precio']}\n"
                  f"        Marca: {datos['marca']}\n"
                  f"        Tipo: {datos['tipo']})\n\n")


def interfaz():
    cargar_figuras()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar figura")
        print("2. Mostrar figuras")
        print("3. Eliminar figura")
        print("4. Guardar figuras")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la figura: ")
            precio = input("Precio de la figura: ")
            tipo = input("Tipo (futbol, heroe, villano): ")
            marca = input("Marca: ")
            agregar_figura(nombre, precio, tipo, marca)

        elif opcion == "2":
            Mostrar_figuras()

        elif opcion == "3":
            id = input("ID de la figura a eliminar: ")
            eliminar_figura(id)

        elif opcion == "4":
            Guardar_figuras()

        elif opcion == "5":
            Guardar_figuras()
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente de nuevo\n")

interfaz()