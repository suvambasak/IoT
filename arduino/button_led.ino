
int button_value=0;
int button=3;
int led=2;

void setup()
{
	pinMode(button,INPUT);
	pinMode(led,OUTPUT);
}

void loop()
{
	button_value = digitalRead(button);
	if(button_value){
		digitalWrite(led,HIGH);
	}else{
		digitalWrite(led,LOW);
	}
}
