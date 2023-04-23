
# Importamos paho client de mqtt para poder realizar el programa
import paho.mqtt.client as mqtt

import random
import time
# Establecemos codigos de seguidad de los Rdif o nfc
# Generar tres UID de 16 bytes (128 bits) aleatoria para introducirlas como ejemplos de intentos de intrusion.
uid = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
uid2 = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
uid3 = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
# Asignar la UID a la variable nivel1
Nivel1 = "F24944D82E1F3B7F"
# Asignar la UID a la variable nivel2
Nivel2 = "C89BC93E86CFE080"
# Asignar la UID a la variable nivel3
Nivel3 = "BACCF33591C2DEB7"

# Nos conectamos como cliente de mosquito con el mqtt 
client = mqtt.Client()
# Asignamos los datos del cliente, en este caso tambien podriamos cambiar localhost seguido del puerto y el tiempo que tardara en desconectarse automaticamente el cliente.
client.connect("localhost", 1883, 60)
# Publicamos en el topic "puerta1" (simulacion de entrada de RFID) de los 3 niveles, Se espera acceso concedido en todos.
# El time.sleep lo que hara sera aleatorizar un valor entre 2 y 5 y esperar ese tiempo en segundos para simular unas entradas mas realistas.
client.publish("Puerta1", Nivel1)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta1", Nivel2)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta1", Nivel3)
# Publicamos en el topic "puerta2" (simulacion de entrada de RFID) de los 3 niveles, Se espera acceso en niveles 2 y 3.
# El time.sleep lo que hara sera aleatorizar un valor entre 2 y 5 y esperar ese tiempo en segundos para simular unas entradas mas realistas.
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta2", Nivel1)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta2", Nivel2)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta2", Nivel3)
time.sleep(random.uniform(2, 5)) 
# Publicamos en el topic "puerta3" (simulacion de entrada de RFID) de los 3 niveles, Se espera unicamente aceso en el nivel 3.
# El time.sleep lo que hara sera aleatorizar un valor entre 2 y 5 y esperar ese tiempo en segundos para simular unas entradas mas realistas.
client.publish("Puerta3", Nivel1)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta3", Nivel2)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta3", Nivel3)
# Publicamos en el topic "puerta1","puerta2","puerta3" (simulacion de entrada de RFID) Se espera que todos sean denegados.
# El time.sleep lo que hara sera aleatorizar un valor entre 2 y 5 y esperar ese tiempo en segundos para simular unas entradas mas realistas.
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta1", uid)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta2", uid2)
time.sleep(random.uniform(2, 5)) 
client.publish("Puerta3", uid3)

# Forzamos una desconexion al cliente
client.disconnect()
