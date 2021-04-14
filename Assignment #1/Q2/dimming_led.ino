
/*	This is a default program--
	Use File->Load Prog to load a different program
*/

int led=3;
int knob=0;

void setup()
{
	pinMode(led,OUTPUT);
}

void loop()
{
	int value;
	value = analogRead(knob);
	value = map(value,1,1024,1,255);
	analogWrite(led, value);	
}
