
// library
#include <Servo.h>

// Signal pin to control servo.
int servo_pin = 9;
// Position of servo.
int servo_pos = 0;
int knob = 0;
// servo object
Servo my_servo;

void setup()
{
	Serial.begin(9600);
	// Attach the signal pin
	my_servo.attach(servo_pin);
}

void loop()
{
	int input;
	// Take analog input.
	input = analogRead(knob);
	// Range conversion.
	servo_pos = map(input, 1, 1024, 1, 100);

	Serial.println(servo_pos);
	delay(100);
	// Rotate servo moto to specified position.
	my_servo.write(servo_pos);
}
