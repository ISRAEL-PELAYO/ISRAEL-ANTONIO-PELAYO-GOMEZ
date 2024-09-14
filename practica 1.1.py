from collections import deque

# Función de BFS para encontrar personas conectadas y niveles de amistad
def bfs(red_social, persona_inicial):
    visitado = set()  # Personas ya visitadas
    cola = deque([(persona_inicial, 0)])  # Cola para recorrer personas (nivel de separación incluido)
    niveles = {}  # Diccionario para contar personas por nivel de separación

    while cola:
        persona, nivel = cola.popleft()  # Saca la persona y el nivel de la cola

        if persona not in visitado:
            visitado.add(persona)  # Marca la persona como visitada

            # Cuenta cuantas personas hay en este nivel de separacion
            if nivel in niveles:
                niveles[nivel] += 1
            else:
                niveles[nivel] = 1

            # Añade a la cola todas las personas conectadas (amigos) que no hayan sido visitadas
            for amigo in red_social[persona]:
                if amigo not in visitado:
                    cola.append((amigo, nivel + 1))

    return niveles, visitado

# Red de amigos (grafo)
red_social = {
    'ricardo': {'dan', 'carlos', 'diana'},
    'dan': {'ricardo', 'eva', 'frank'},
    'carlos': {'ricardo', 'grecia'},
    'diana': {'ricardo', 'ian'},
    'eva': {'dan', 'arleth'},
    'frank': {'dan'},
    'grecia': {'carlos'},
    'ian': {'diana'},
    'arleth': {'eva'}
}

# Pide al usuario la persona inicial para la busqueda
persona_inicial = input("Introduce el nombre de la persona para comenzar la búsqueda: ")

# Ejecuta la búsqueda en anchura (BFS) desde la persona inicial
niveles, personas_conectadas = bfs(red_social, persona_inicial)

# Muestra los resultados
print(f"\nPersonas conectadas a {persona_inicial}: {len(personas_conectadas)}")
print(f"Niveles de separación:")
for nivel, cantidad in niveles.items():
    print(f"Nivel {nivel}: {cantidad} persona(s)")
