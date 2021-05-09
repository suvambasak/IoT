
void setup()
{
	Serial.begin(9600);
}

void loop()
{
	if(Serial.available()){
		char val = Serial.read();
		Serial.print(val);
	}
}
