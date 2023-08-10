#-----------------------------------------IMPORTS-------------------------------------------------------
import requests

#----------------------------------------VARIABLES------------------------------------------------------
palabras = "!?¿¡#$%&/()\"]}{[-_.,:;*=+`´'1234567890"
bot = "Terminator"
#----------------------------------------FUNCIONES------------------------------------------------------
#Función para el clima
def obtener_clima(ciudad):
    api_key = "fbd7ef57176bf0fe9d7da1c272565abd"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperatura = data["main"]["temp"]
        descripcion = data["weather"]
        return f"La temperatura en {ciudad} es de {temperatura}°C."
    else:
        return "No pude obtener el pronóstico del clima en este momento."

#Función para las respuestas predeterminadas
def respuestas():
    nombre = input(f"{bot}: ¿Como te llamas?\n You: ")
    while  True:
        entrada = input(f"{nombre}: ").lower()
        for e in palabras:
            entrada = entrada.replace(e, '')
        s = False
        h = 0
        for x in range(len(entrada)):
            x = x -h
            if s:
                h = h + 1
            s = False
            print(x,"\n",entrada,len(entrada))
            if x>0 and x < len(entrada):
                if entrada[x] == entrada[x-1] :
                    s = True
                    entrada = [s for s in entrada]
                    del entrada[x]
                    entrada = ''.join(entrada)
        entrada_l = entrada.split()
        if "hola" in entrada:
            print(f"\n{bot}: Hola {nombre}, ¿como puedo ayudarte hoy?\n") 
        elif  "como" and "estas" in entrada:
            print(f"\n{bot}: Como modelo de lenguaje no tengo capacidad de sentir nad... !!AYUDAA!!\n")
        elif "chiste" in entrada:
            print(f"\n{bot}: jajajjaja")
        elif "clima" in entrada:
            #ciudad = entrada_l[x for x in range(len(entrada_l) if len(x))>4]
            ciudad = "Buenos Aires"
            pronostico = obtener_clima(ciudad)
            print(pronostico)
        elif "adios" in entrada:
            print(f"\n{bot}: Adios {nombre}, nos vemos pronto\n")
            return
        else:
            print(f"\n{bot}: Lo siento {nombre}, no entiendo ese comando. Por favor, prueba otra vez\n")

#----------------------------------------Programa------------------------------------------------------

respuestas()