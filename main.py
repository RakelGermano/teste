from flask import Flask, render_template, request
# import requests
from flask_cors import CORS
import paho.mqtt.client as MqttClient
from threading import Thread

Config_broker = {
"HOST": "mqtt.eclipseprojects.io",  # broker publico online :  https://iot.eclipse.org/projects/sandboxes/
"PORT":1883, #porta do broker publico
"CLIENT_ID":"flask", 
"KEEPALIVE":3, #define intervalos de tempo para certificar que estar tendo a comunicação
"TOPIC": "Alimentador_Tcc" # define o topico para publicar, Obs: como e publico crie um nome de topico diferente para que outras pessoas nao se concte ao topico
}



app = Flask(__name__)
mqttClient = MqttClient.Client(MqttClient.CallbackAPIVersion.VERSION2, client_id=Config_broker["CLIENT_ID"])

CORS(app)




#funçoes calbacks

def on_connect(client, userdata, flags, reason_code , properties):

    print(f"conectado com o broker. no HOST:{Config_broker['HOST']}, PORTA:{Config_broker['PORT']}")

    if reason_code == 0:
        try:
            client.subscribe(topic=Config_broker["TOPIC"])
            # print(f"inscrito ao topico:{str(Config_broker["TOPIC"])}")

        except:
            print("falha ao se inscrever no topico!")       
    return 0


def on_publish(client, userdata, mid, reason_code, properties):
    print("Mensagem publicada com sucesso")
    return 0



# Rotas

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/ligar1", methods=["POST"])
def ligar_led1():

    mqttClient.publish(topic=Config_broker["TOPIC"], payload="ligar1")


    return "Ok"

@app.route("/desligar1", methods=["POST"])
def desligar_led1():
    mqttClient.publish(topic=Config_broker["TOPIC"], payload="desligar1")

    return "Ok"

@app.route("/ligar2", methods=["POST"])
def ligar_led2():

    mqttClient.publish(topic=Config_broker["TOPIC"], payload="ligar2")

    return "Ok"

@app.route("/desligar2", methods=["POST"])
def desligar_led2():

    mqttClient.publish(topic=Config_broker["TOPIC"], payload="desligar2")

    return "Ok"



def mqtt_loop():
    # iniciar comunicaçao mqtt

    try:
        mqttClient.connect(host=Config_broker["HOST"], port=Config_broker["PORT"],keepalive=Config_broker["KEEPALIVE"])
        mqttClient.on_connect = on_connect
        mqttClient.on_publish = on_publish


    except:
        print("erro ao se conectar!")


    while True:
       mqttClient.loop(timeout=1)



if __name__ == "__main__":

    mqtt_thread = Thread(target=mqtt_loop)
    mqtt_thread.start()

    app.run(debug=True, host="0.0.0.0")



















# from flask import Flask, render_template, request
# import requests
# from flask_cors import CORS


# app = Flask(__name__)

# CORS(app)

# NODEMCU_IP = "192.168.15.111" # Substitua pelo IP do seu NodeMCU

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/ligar1", methods=["POST"])
# def ligar_led1():
#     requests.get(f"http://{NODEMCU_IP}/ligar1")
#     return "Ok"

# @app.route("/desligar1", methods=["POST"])
# def desligar_led1():
#     requests.get(f"http://{NODEMCU_IP}/desligar1")
#     return "Ok"

# @app.route("/ligar2", methods=["POST"])
# def ligar_led2():
#     requests.get(f"http://{NODEMCU_IP}/ligar2")
#     return "Ok"

# @app.route("/desligar2", methods=["POST"])
# def desligar_led2():
#     requests.get(f"http://{NODEMCU_IP}/desligar2")
#     return "Ok"

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")
