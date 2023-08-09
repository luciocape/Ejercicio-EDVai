#-----------------------------------------IMPORTS-------------------------------------------------------
import requests

#----------------------------------------VARIABLES------------------------------------------------------
palabras = "!?¿¡#$%&/()\"]}{[-_.,:;*= '1234567890"
bot = "Terminator"

#----------------------------------------FUNCIONES------------------------------------------------------

#Función para el clima
def obtener_clima(ciudad):
    api_key = "TU_CLAVE_DE_API"  # Reemplaza con tu clave de API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperatura = data["main"]["temp"]
        descripcion = data["weather"][0]["description"]
        return f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C."
    else:
        return "No pude obtener el pronóstico del clima en este momento."

# Ejemplo de uso






#Función para las respuestas predeterminadas
def respuestas():
    nombre = input(f"{bot}: ¿Como te llamas?\n You: ")
    while  True:
        entrada = input(f"{nombre}: ").lower()
        for e in palabras:
            entrada = entrada.replace(e, '')
        for x in range(len(entrada)):
            if x>0 and x<len(entrada):
                if entrada[x] == entrada[x-1] :
                    entrada = [s for s in entrada]
                    del entrada[x-1]
                    entrada = ''.join(entrada)
        if "hola" in entrada:
            print(f"\n{bot}: Hola {nombre}, ¿como puedo ayudarte hoy?\n") 
        elif  "como" and "estas" in entrada:
            print(f"\n{bot}: Como modelo de lenguaje no tengo capacidad de sentir nad... !!AYUDAA!!\n")
        elif "chiste" in entrada:
            print(f"\n{bot}: jajajjaja")
        elif "clima" in entrada:
            
            print(f"\n{bot}: gopo")
        elif "adios" in entrada:
            print(f"\n{bot}: Adios {nombre}, nos vemos pronto\n")
            return
        else:
            print(f"\n{bot}: Lo siento {nombre}, no entiendo ese comando. Por favor, prueba otra vez\n")
ciudad = "NOMBRE_DE_LA_CIUDAD"
pronostico = obtener_clima(ciudad)
print(pronostico)
respuestas()