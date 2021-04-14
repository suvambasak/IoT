
int knob=0;
int volt=0;

int count;

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	int new_range;
	volt=analogRead(knob);
	new_range = map(volt,1,1024,1,100);
	Serial.println(new_range);
	delay(1000);
}
