
int knob=0;
int volt=0;

void setup()
{
	// Starts serial communication.
	Serial.begin(9600);
}

void loop()
{
	int new_range;
	// Read the analog value.
	volt = analogRead(knob);
	// conversion factor to return a range from 0 to 100
	new_range = volt*0.0977;
	// Show the value in Serial monitor.
	Serial.println(new_range);
	delay(1000);
}
