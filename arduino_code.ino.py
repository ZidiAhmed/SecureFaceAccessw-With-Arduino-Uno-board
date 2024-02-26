const int doorPin = 13;  // Digital pin connected to the door mechanism
char serialData;

void setup() {
  Serial.begin(9600);
  pinMode(doorPin, OUTPUT);
  digitalWrite(doorPin, LOW);  // Initially, keep the door closed
}

void loop() {
  if (Serial.available() > 0) {
    serialData = Serial.read();
    if (serialData == 'O') {
      openDoor();
    }
  }
}

void openDoor() {
  digitalWrite(doorPin, HIGH);  // Open the door
  delay(2000);  // Keep the door open for 2 seconds (adjust as needed)
  digitalWrite(doorPin, LOW);  // Close the door
}
