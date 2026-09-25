class Chatbot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.base_conocimiento = {
            "hola" : "¡Hola! ¿En que puedo ayudarte?",
            "adios" : "¡Hasta luego, que tengas un buen dia!",
            "como estas" : "Estoy funcionando corectamente, gracias por preguntar",
            "quien eres" : "Soy un chatbot creado para practicar POO en PYthon."
        }
        self.historial = []

    def responder(self, mensaje):
        mensaje = mensaje.lower().strip()
        self.historial.append(mensaje)

        for clave, respuesta in  self.base_conocimiento.items():
            if clave in mensaje:
                return respuesta

        return "No entendi tu mensaje, ¿podrías reformularlo?"

    def agregar_conocimiento(self, clave, respuesta):
        self.base_conocimiento[clave.lower()] = respuesta

    def main():
        bot = chatbot("Asistente SNPP")
        print(f"{bot.nombre}: ¡Hola! Escribe 'salir' para terminar la conversacion.")

        while True:
            entrada = input("Tú: ")
            if entrada.lower() == "salir":
                print(f"{bot.nombre}: ¡Hasta pronto!")
                break


            respuesta = bot.responder(entrada)
            print(f"{bot.nombre}: {respuesta}")

    if __name__ == "__main__":
        main()