import paho.mqtt.client as mqtt

# Define Variables
MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "ShadowPlay"
MQTT_MSG = "Excelciore"


# Define on_connect event Handler
def on_connect(client, userdata, flags, rc):
	#Subscribe to a the Topic
	client.subscribe(MQTT_TOPIC, 0)
	print("Connected with result code "+str(rc))

# Define on_subscribe event Handler
def on_subscribe(client, obj, mid, granted_qos):
    print ("Topic Subscribed")
	

# Define on_message event Handler
def on_message(client, userdata, message):
	print("%s %s" % (message.topic, message.payload))
	

# Initiate MQTT Client
client = mqtt.Client()

# Register Event Handlers
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

# Connect with MQTT Broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL )


# Continue the network loop
client.loop_forever()



