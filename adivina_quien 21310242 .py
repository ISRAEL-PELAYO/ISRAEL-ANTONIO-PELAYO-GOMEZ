import json
import os

# Archivo JSON para almacenar personajes
DB_FILE = "personajes.json"

# Cargar o inicializar base de datos de personajes
def cargar_personajes():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

# Guardar base de datos de personajes
def guardar_personajes(personajes):
    with open(DB_FILE, "w") as f:
        json.dump(personajes, f, indent=4)

# Función para hacer preguntas basadas en atributos
def hacer_pregunta(atributo):
    respuesta = input(f"¿El personaje {atributo}? (s/n): ").lower()
    return respuesta == 's'

# Filtrar personajes basados en respuestas
def filtrar_personajes(personajes, atributos_positivos):
    candidatos = personajes.copy()
    for nombre, atributos in personajes.items():
        for atributo in atributos_positivos:
            if atributo not in atributos:
                candidatos.pop(nombre, None)
                break
    return candidatos

# Función para adivinar personaje
def adivinar_personaje():
    personajes = cargar_personajes()
    if not personajes:
        print("No hay personajes en la base de datos. Por favor, añade uno nuevo.")
        agregar_personaje()
        return

    atributos_positivos = []
    posibles_personajes = personajes.copy()

    while len(posibles_personajes) > 1:
        # Obtener lista de todos los atributos posibles
        atributos_disponibles = {attr for attrs in posibles_personajes.values() for attr in attrs if attr.strip()}
        
        # Elegir un atributo para preguntar
        for atributo in atributos_disponibles:
            if hacer_pregunta(atributo):
                atributos_positivos.append(atributo)
                posibles_personajes = filtrar_personajes(posibles_personajes, atributos_positivos)
                break
            else:
                # Si el usuario responde 'n' a todos, eliminar personajes con ese atributo
                posibles_personajes = {nombre: attrs for nombre, attrs in posibles_personajes.items() if atributo not in attrs}

        # Si no quedan personajes posibles después del filtrado
        if not posibles_personajes:
            print("No pude adivinar. Vamos a añadir un nuevo personaje.")
            agregar_personaje()
            return

    # Resultado: si hay un solo candidato
    if len(posibles_personajes) == 1:
        personaje = list(posibles_personajes.keys())[0]
        print(f"Creo que tu personaje es: {personaje}")
    else:
        print("No pude adivinar. Vamos a añadir un nuevo personaje.")
        agregar_personaje()

# Función para agregar un nuevo personaje
def agregar_personaje():
    personajes = cargar_personajes()
    nombre = input("¿Cuál es el nombre del personaje?: ")
    atributos = []
    
    while True:
        atributo = input("Añade un atributo (escribe 'fin' para terminar): ").lower()
        if atributo == "fin":
            break
        if atributo.strip():  # Asegurarse de que el atributo no esté vacío
            atributos.append(atributo)
        else:
            print("El atributo no puede estar vacío. Intenta de nuevo.")
    
    personajes[nombre] = atributos
    guardar_personajes(personajes)
    print("¡Personaje añadido con éxito!")

# Menú principal
def menu():
    while True:
        print("\nBienvenido al juego de 'Adivina Quién'")
        print("1. Jugar")
        print("2. Añadir personaje")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            adivinar_personaje()
        elif opcion == "2":
            agregar_personaje()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
