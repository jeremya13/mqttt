import paho.mqtt.client as mqttClient
import time
import random
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, message):
    print("Message received: "  + str(message.topic) + " : " + str(message.payload))

def on_log(client, userdata, level, string):
    print(string)
 
Connected = False   #global variable for the state of the connection

# Register ke online broker, ex: CloudMQTT atau ke service MQTT gratis lainnya
# Bisa juga menggunakan Mosquitto untuk offline mqtt broker
# Credentialnya dapat diisi di bagian ini.
# Note: 
# pada contoh ini, broker hanya dapat diakses oleh 5 aktif koneksi 
broker_address = "180.250.7.185"  #Broker address
port = 21283                         #Broker port
user = "tester1"                    #Connection username
password = "itbstikombali11"            #Connection password

# Publish name dapat diubah, sesuai dengan yg diinginkan 
name_pubs = "jee"

client = mqttClient.Client("learn_" + str(random.randint(1,999)))   #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.on_subscribe = on_subscribe
client.on_log = on_log

client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(1)

client.subscribe(name_pubs)

try:
    while True:     
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
