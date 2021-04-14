
int knob=0;
int volt=0;

int count;

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	volt=analogRead(knob);
	Serial.println(volt);
	delay(1000);
}
