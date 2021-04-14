
int transducers_lower_value=0;
int transducers_upper_value=0;
int transducers_lower=5;
int transducers_upper=6;
int pump1=2;
int pump2=4;

void setup()
{
	pinMode(transducers_lower,INPUT);
	pinMode(transducers_upper,INPUT);
	pinMode(pump1,OUTPUT);
	pinMode(pump2,OUTPUT);
}

void loop()
{
	transducers_lower_value = digitalRead(transducers_lower);
	transducers_upper_value = digitalRead(transducers_upper);
	
	if(transducers_upper_value){
		digitalWrite(pump1,HIGH);
		digitalWrite(pump2,HIGH);
	}else if(!transducers_lower_value){
		digitalWrite(pump1,LOW);
		digitalWrite(pump2,LOW);
	}else{
		digitalWrite(pump1,HIGH);
		digitalWrite(pump2,LOW);
	}
}
