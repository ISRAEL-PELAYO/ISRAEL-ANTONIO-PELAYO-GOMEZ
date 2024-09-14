# Estructura de carpetas (grafo)
estructura_carpetas = {
    'carpeta_Raiz': ['documentos', 'fotos', 'musica'],
    'documentos': ['trabajo', 'proyectos'],
    'fotos': ['vacaciones', 'familia'],
    'musica': ['rock', 'clásica'],
    'trabajo': ['informe.pdf', 'resumen.docx'],
    'proyectos': ['proyecto1', 'proyecto2'],
    'vacaciones': ['foto1.jpg', 'foto2.jpg'],
    'familia': ['cumpleaños.jpg'],
    'rock': ['cancion1.mp3', 'cancion2.mp3'],
    'clásica': ['sinfonía.mp3'],
    'proyecto1': [],
    'proyecto2': [],
    'informe.pdf': [],
    'resumen.docx': [],
    'foto1.jpg': [],
    'foto2.jpg': [],
    'cumpleaños.jpg': [],
    'cancion1.mp3': [],
    'cancion2.mp3': [],
    'sinfonía.mp3': []
}

visitado = set()

# Función DFS para explorar carpetas y archivos
def explorador_carpetas(visitado, estructura_carpetas, carpeta_actual):
    if carpeta_actual not in visitado:
        visitado.add(carpeta_actual)  # Marcamos la carpeta o archivo como visitado
        for contenido in estructura_carpetas[carpeta_actual]:
            print(f"Explorando: {contenido} dentro de {carpeta_actual}")
            explorador_carpetas(visitado, estructura_carpetas, contenido)  # Llamada recursiva para explorar subcarpetas o archivos

# Solicitar al usuario la carpeta inicial para comenzar la exploración
carpeta_inicial = input("Introduce la carpeta inicial para comenzar la exploración: ")

# Ejecutamos la búsqueda en profundidad (DFS) desde la carpeta inicial
explorador_carpetas(visitado, estructura_carpetas, carpeta_inicial)
