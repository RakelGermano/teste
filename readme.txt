Broker Publico no eclipse
https://iot.eclipse.org/projects/sandboxes/

Host = mqtt.eclipseprojects.io
porta = 1883





Para resceber as mensagens que foram enviadas pelo servidor flask ao broker , precisa instalar o mosquitto

1 - instale o mosquitto
    https://mosquitto.org/download/

2 - abra o terminal e execute o comando
    mosquitto_sub -h mqtt.eclipseprojects.io -p 1883 -t Alimentador_Tcc


assim quando clicar em qualquer botao vc verar no terminal a mensagens recebida pelo broker