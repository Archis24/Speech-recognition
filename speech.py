# Importamos las bibliotecas necesarias
import speech_recognition as sr  # Permite reconocer la voz del usuario
import random  # Permite elegir palabras al azar

# Lista de palabras que el usuario debe pronunciar en inglés
words = ["太陽","月", "星", "空", "雲"]  #como se pronuncian, Taiyō ,tsuki, hoshi, sora, kumo
# Palabras pero en ingles
#sun, moon, star, sky, cloud

# Función que escucha lo que el usuario dice
def listen():
    with sr.Microphone() as source:  # Abre el micrófono para escuchar
        print("🎤 Di la palabra en voz alta...")  # Pide al usuario que hable
        audio = sr.Recognizer().listen(source)  # Graba la voz del usuario
    
    # Convierte el audio en texto usando reconocimiento de voz en el idioma japonés
    # (aunque la palabra es en inglés, el reconocimiento se hace en japonés)
    # Esto es un error, ya que el idioma debería ser inglés
    return sr.Recognizer().recognize_google(audio, language="ja-JP").lower()

# Función principal del juego
def game():
    score = 0  # Inicializa la puntuación en 0
    for _ in range(3):  # Repite el juego 3 veces
        word = random.choice(words)  # Escoge una palabra al azar
        print(f"🔵 Pronuncia: {word}")  # Muestra la palabra en pantalla

        try:
            # Compara lo que dijo el usuario con la palabra correcta
            if listen() == word:
                print("✅ ¡Bien!")  # Si es correcto, muestra un mensaje positivo
                score += 1  # Suma 1 punto
            else:
                print("❌ Inténtalo de nuevo.")  # Si es incorrecto, pide que lo intente otra vez
        except:
            print("❌ No entendí.")  # Si hay un error, muestra un mensaje de error
    
    # Muestra la puntuación final
    print(f"🎉 Puntos: {score}/3")

# Mensaje de bienvenida y ejecución del juego
print("🎤 ¡Bienvenido!")  
game()  # Llama a la función del juego para empezar
