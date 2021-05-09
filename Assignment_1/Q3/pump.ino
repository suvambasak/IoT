// Value from two transducer
int transducers_lower_value=0;
int transducers_upper_value=0;

// Two transducers
int transducers_lower=5;
int transducers_upper=6;

// Two pump
int pump1=2;
int pump2=4;

void setup()
{
	// Transducers set to input mode
	pinMode(transducers_lower,INPUT);
	pinMode(transducers_upper,INPUT);

	// Pumps are in output mode.
	pinMode(pump1,OUTPUT);
	pinMode(pump2,OUTPUT);
}

void loop()
{
	// Get the current value from two transducers_lower
	transducers_lower_value = digitalRead(transducers_lower);
	transducers_upper_value = digitalRead(transducers_upper);
	
	// If water level above the HIGH (High transducers) turn on both pump.
	if(transducers_upper_value){
		digitalWrite(pump1,HIGH);
		digitalWrite(pump2,HIGH);
	}
	// If water level below the LOW (Lower transducers) trun off both pump.
	else if(!transducers_lower_value){
		digitalWrite(pump1,LOW);
		digitalWrite(pump2,LOW);
	}
	// If water level in middle of both transducers keep one pump on.
	else{
		digitalWrite(pump1,HIGH);
		digitalWrite(pump2,LOW);
	}
	
	// Wait for 1000 msecs
	delay(1000);
}
