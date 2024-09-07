import paho.mqtt.subscribe as subscribe

# msg = subscribe.simple("MQTT Examples", hostname="localhost", port=1883)
# print("%s %s" % ( msg.topic, msg.payload.decode('utf-8')))

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    userdata["message_count"] += 1
    # if userdata["message_count"] >= 5:
        # client.disconnect()

subscribe.callback(on_message_print, "MQTT Examples", hostname="localhost", port=1883, userdata={"message_count":0})
