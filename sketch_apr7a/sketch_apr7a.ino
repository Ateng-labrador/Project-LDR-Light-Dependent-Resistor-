int LDR_pin = A0;
int LED_pin = 9;
int brightness = 0;
int LDR_value;


void setup() {
  Serial.begin(9600);
  pinMode(LED_pin, OUTPUT);
  analogWrite(LED_pin, brightness);
}

void loop() {
  LDR_value = analogRead(LDR_pin);
  Serial.println(LDR_value);

  delay(1000);
}
