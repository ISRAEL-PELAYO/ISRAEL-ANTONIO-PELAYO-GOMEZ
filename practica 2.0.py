
#ISRAEL ANTONIO PELAYO GOMEZ 21310242 7F

import json
import os

# Archivo JSON para simular la base de datos de conocimientos
DB_FILE = "knowledge_base.json"

# Crear la base de datos inicial si no existe
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({
            "hola": "hola, cómo estas?",
            "¿como estás?": "estoy bien, ¿y tú como andas?",
            "¿de qué te gustaría hablar?": "Puedo hablar sobre cualquier cosa, pregúntame algo"
        }, f)

# Función para cargar la base de datos
def load_knowledge_base():
    with open(DB_FILE, "r") as f:
        return json.load(f)

# Función para guardar una nueva entrada en la base de datos
def save_to_knowledge_base(question, answer):
    knowledge_base = load_knowledge_base()
    knowledge_base[question] = answer
    with open(DB_FILE, "w") as f:
        json.dump(knowledge_base, f)

# Función principal del chat
def chat():
    print("Bienvenido al chat. Puedes empezar a conversar algo conmigo :)")
    
    while True:
        # Obtener la entrada del usuario
        user_message = input("Tú: ")
        
        # Cargar la base de datos de conocimientos
        knowledge_base = load_knowledge_base()
        
        # Buscar si existe una respuesta en la base de datos
        response = knowledge_base.get(user_message)
        
        if response:
            print(f"Bot: {response}")
        else:
            print("Bot: No sé cómo responder a eso. ¿Me podrías enseñar la respuesta por favor?")
            new_answer = input("Enséñame: ")
            
            # Guardar la nueva pregunta y respuesta en la base de datos
            save_to_knowledge_base(user_message, new_answer)
            print(f"Bot: Gracias, he aprendido que '{user_message}' se responde con '{new_answer}'.")

# Iniciar el chat
if __name__ == '__main__':
    chat()

