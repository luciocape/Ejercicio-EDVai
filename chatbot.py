palabras = "!?¿¡#$%&/()\"]}{[-_.,:;*= '1234567890"
bot = "Terminator"
#Función para las respuestas predeterminadas
def respuestas():
    nombre = input(f"{bot}: ¿Como te llamas?\n You: ")
    while  True:
        entrada = input(f"{nombre}: ").lower()
        for e in palabras:
            entrada = entrada.replace(e, '')
        for x in range(len(entrada)):
            if entrada[x] == entrada[x-1] and x>0:
                del entrada[x -1]
        if "hola" in entrada:
            print(f"\n{bot}: Hola {nombre}, ¿como puedo ayudarte hoy?\n") 
        elif  "comoestas" in entrada:
            print(f"\n{bot}: Como modelo de lenguaje no tengo capacidad de sentir nad... !!AYUDAA!!\n")
        elif "chiste" in entrada:
            print(f"\n{bot}: jajajjaja")
        elif "cualeslatemperatura" in entrada:
            print(f"\n{bot}: gopo")
        elif "adios" in entrada:
            print(f"\n{bot}: Adios {nombre}, nos vemos pronto\n")
            return
        else:
            print(f"\n{bot}: Lo siento {nombre}, no entiendo ese comando. Por favor, prueba otra vez\n")

respuestas()