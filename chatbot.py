import re
#Función para las respuestas predeterminadas
def respuestas-p():
    while  True:
        entrada-nombre = input("Como te llamas")
    entrada = input().lower().lstrip().rstrip()
    patron = "[\W]+"
    regex = re.compile(patron)
    resultado = regex.sub("",entrada)
    print(resultado)
    entradas = entrada.split()
    if entrada == "hola":
        print(f"Hola {entrada-nombre} , ¿como puedo ayudarte hoy?") 
    elif  entrada == "como estas":
        print("Como modelo de lenguaje no tengo capacidad de sentir nad... !!AYUDAA!!")
    elif "chiste" in entrada:
        print("")
    elif entrada == "Cual es la temperarura"
    elif entrada == "adios":
        print(f"Adios {entrada-nombre}, nos vemos pronto")
        return
    else:
        print("Lo siento, no entiendo ese comando. Por favor, prueba otra vez")
