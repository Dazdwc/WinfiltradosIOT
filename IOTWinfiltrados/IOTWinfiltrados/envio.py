
import paho.mqtt.client as mqtt

#Establecemos c�digos de seguidad de los Rdif o nfc
import random
import time

# Generar una UID de 16 bytes (128 bits) aleatoria
uid = ''.join(random.choice('0123456789ABCDEF') for i in range(16))

# Asignar la UID a la variable nivel1
Nivel1 = "F24944D82E1F3B7F"
Nivel2 = "C89BC93E86CFE080"
Nivel3 = "BACCF33591C2DEB7"
client = mqtt.Client()

client.connect("localhost", 1883, 60)
# Puertas
client.publish("Puerta1", Nivel1)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta2", Nivel1)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta3", Nivel1)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta1", Nivel2)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta2", Nivel2)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta3", Nivel2)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta1", Nivel3)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta2", Nivel3)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta3", Nivel3)
time.sleep(random.uniform(2, 5)) # Espera un tiempo aleatorio entre 2 y 5 segundos
client.publish("Puerta1", uid)

client.disconnect()
