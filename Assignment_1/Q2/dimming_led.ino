int led=3;
int knob=0;

void setup()
{
	pinMode(led,OUTPUT);
}

void loop()
{
	int value;
	
	// Read the analog value
	value = analogRead(knob);
	value = map(value,1,1024,1,255);

	// Dim the LED corresponding input analog value.
	analogWrite(led, value);	
}
