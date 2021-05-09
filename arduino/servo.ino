#include <Servo.h>

int servo_pin=9;
int servo_pos=180;
Servo my_servo;

void setup()
{
	my_servo.attach(servo_pin);
}

void loop()
{
	my_servo.write(servo_pos);
}
