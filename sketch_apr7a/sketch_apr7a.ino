int LDR_pin = A0;
int LED_pin = 9;

float a = 0.5;
float b = 0.002;

int brightness = 0;
int step = 20;
int direction = 1;

int LDR_value;

unsigned long previousMillis = 0;
const long interval = 60000; // 1 menit

void setup(){
  Serial.begin(9600);
  pinMode(LED_pin, OUTPUT);
}

void loop(){
  unsigned long currentMillis = millis();

  // Update tiap 1 menit
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    brightness += step * direction;

    if (brightness >= 220) {
      brightness = 220;
      direction = -1;
    }
    else if (brightness <= 0) {
      brightness = 0;
      direction = 1;
    }

    analogWrite(LED_pin, brightness);
  }

  // LDR tetap dibaca terus (tidak nunggu 1 menit)
  LDR_value = analogRead(LDR_pin);
  float lux = a * exp(b * LDR_value);

  Serial.print("LDR Value: ");
  Serial.print(LDR_value);
  Serial.print(" Lux: ");
  Serial.print(lux);
  Serial.print(" Brightness: ");
  Serial.println(brightness);
}