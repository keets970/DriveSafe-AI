// DriveSafe-AI: Arduino buzzer controller
// Assumes an active buzzer connected to digital pin 8 and GND.
// Python sends '1' to turn the buzzer on and '0' to turn it off.

const int BUZZER_PIN = 8;

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(BUZZER_PIN, HIGH);
    } else if (command == '0') {
      digitalWrite(BUZZER_PIN, LOW);
    }
  }
}
