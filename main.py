import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))


def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("username", "password")

client.connect("broker.hivemq.com", 1883)

client.subscribe("home/topic1")

client.loop_forever()

client.publish("home/topic1/switch", "On")
