int knob=0;
int volt=0;

void setup()
{
	// Starts serial communication.
	Serial.begin(9600);
}

void loop()
{
	// Read the analog input. 
	volt=analogRead(knob);

	// Show the value in Serial monitor.
	Serial.println(volt);
	delay(1000);
}
