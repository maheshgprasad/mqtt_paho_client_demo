# Import package
import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "ShadowPlay"
MQTT_MSG = "Kubuntu is awesome"


# Define on_connect event Handler
def conn (client, userdata, flags, rc):
	print ("Connection to MQTT Message Broker Established")

# Define on_publish event Handler
def pub (client, userdata, mid):
	print ("Message Sent!")

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = pub
mqttc.on_connect = conn

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

# Publish message to MQTT Topic 
mqttc.publish(MQTT_TOPIC,MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()
