
/*	This is a default program--
	Use File->Load Prog to load a different program
*/

int led=13;
int knob=0;

void setup()
{
	pinMode(led,OUTPUT);
}

void loop()
{
	int time;
	time = analogRead(knob);
	digitalWrite(led,HIGH);
	delay(time);
	digitalWrite(led,LOW);
	delay(time);
}
