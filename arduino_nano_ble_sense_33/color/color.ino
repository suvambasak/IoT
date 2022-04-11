#include <Arduino_APDS9960.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!APDS.begin()) {
    Serial.println("Error initializing APDS9960 sensor.");
  }
}

void loop() {

  // check if a color reading is available
  while (! APDS.colorAvailable()) {
    delay(5);
  }
  int r, g, b;

  // read the color
  APDS.readColor(r, g, b);

  if ((r > g) & (r > b))
  {
    digitalWrite(LEDR, LOW);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
  }
  else if ((g > r) & (g > b))
  {
    digitalWrite(LEDG, LOW);
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDB, HIGH);
  }
  else if ((b > g) & (b > r))
  {
    digitalWrite(LEDB, LOW);
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
  }
  else
  {
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, HIGH);
  }


  // print the values
  Serial.print("Red light = ");
  Serial.println(r);
  Serial.print("Green light = ");
  Serial.println(g);
  Serial.print("Blue light = ");
  Serial.println(b);
  Serial.println();

  delay(500);
}
