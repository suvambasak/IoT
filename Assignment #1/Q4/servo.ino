#include <Servo.h>

int servo_pin=9;
int servo_pos=100;
int knob=0;
Servo my_servo;

void setup()
{
	Serial.begin(9600);
	my_servo.attach(servo_pin);
}

void loop()
{
	int input;
	input = analogRead(knob);
	servo_pos = map(input,1,1024,1,100);
	Serial.println(servo_pos);
	delay(100);
	my_servo.write(servo_pos);
}
