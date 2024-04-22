#include <dummy.h>

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "RENATA";
const char* password = "010507ggr!";

ESP8266WebServer server(80);

const int ledPin1 = D1; // Pino do primeiro LED
const int ledPin2 = D2; // Pino do segundo LED
bool ledState1 = false; // Estado inicial do primeiro LED
bool ledState2 = false; // Estado inicial do segundo LED

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);

  Serial.begin(115200);
  //Serial.println("Connecting to WiFi..");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  Serial.println(WiFi.localIP());

  server.on("/", []() {
    server.send(200, "text/plain", "Hello from NodeMCU!");
  });

  server.on("/ligar1", []() {
    ledState1 = true;
    digitalWrite(ledPin1, HIGH);
    server.send(200, "text/plain", "LED 1 Ligado");
  });

  server.on("/desligar1", []() {
    ledState1 = false;
    digitalWrite(ledPin1, LOW);
    server.send(200, "text/plain", "LED 1 Desligado");
  });

  server.on("/ligar2", []() {
    ledState2 = true;
    digitalWrite(ledPin2, HIGH);
    server.send(200, "text/plain", "LED 2 Ligado");
  });

  server.on("/desligar2", []() {
    ledState2 = false;
    digitalWrite(ledPin2, LOW);
    server.send(200, "text/plain", "LED 2 Desligado");
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
