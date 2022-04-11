#include <Arduino_LPS22HB.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial);

  if (!BARO.begin()) {
    Serial.println("Failed to initialize pressure sensor!");
    while (1);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  float pressure = BARO.readPressure();

  float altitude = 44330 * ( 1 - pow(pressure/101.325, 1/5.255) );

  Serial.print("pressure = ");
  Serial.print(pressure);
  Serial.println(" kPa");
  
  Serial.print("altitude = ");
  Serial.print(altitude);
  Serial.println(" m");


  delay(1000);
}
