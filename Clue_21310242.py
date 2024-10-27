import random
#Personajes, ubicaciones y armas
personajes = [
    {"nombre": "sr. pelayo", "profesion": "Mecánico"},
    {"nombre": "sra. antonia", "profesion": "Abogada"},
    {"nombre": "prof. wacho", "profesion": "Profesor"},
    {"nombre": "srita. aziel", "profesion": "Ingeniera"},
    {"nombre": "coronel mau", "profesion": "Militar"}
]

ubicaciones = ["Casa", "Hotel", "Cuarto", "Cocina", "Jardín"]
armas = ["Cuchillo", "Pistola", "Veneno", "Cuerda", "Llave inglesa"]

#Seleccionar culpable, ubicacion y arma correcta al azar
culpable_correcto = random.choice(personajes)
ubicacion_correcta = random.choice(ubicaciones)
arma_correcta = random.choice(armas)

#Bienvenida
print("Bienvenido al juego Clue: Among Us")
print("Tu objetivo es adivinar quién es el culpable, dónde ocurrió el crimen y con qué arma")
print("Opciones:")
print(f"Personajes: {[p['nombre'] for p in personajes]}")
print(f"Ubicaciones: {ubicaciones}")
print(f"Armas: {armas}")

#Funcion para hacer una adivinanza
def hacer_adivinanza():
    print("\nRealiza tu suposición:")
    culpable = input("¿Quién crees que es el culpable? ")
    ubicacion = input("¿En qué lugar ocurrió el crimen? ")
    arma = input("¿Cuál fue el arma usada? ")

    # Verificar la adivinanza
    correcto = True
    if culpable != culpable_correcto["nombre"]:
        print("El personaje no es correcto")
        correcto = False
    if ubicacion != ubicacion_correcta:
        print("La ubicación no es correcta")
        correcto = False
    if arma != arma_correcta:
        print("El arma no es correcta")
        correcto = False

    return correcto

#Ciclo del juego
intentos = 5
while intentos > 0:
    print(f"\nIntentos restantes: {intentos}")
    if hacer_adivinanza():
        print("\n¡Felicidades! Has resuelto el misterio correctamente")
        break
    else:
        print("Intenta de nuevo")
        intentos -= 1

if intentos == 0:
    print("\nSe te acabaron los intentos.")
    print(f"La respuesta correcta era: {culpable_correcto['nombre']} que es ({culpable_correcto['profesion']}) en la {ubicacion_correcta} con el {arma_correcta}")
