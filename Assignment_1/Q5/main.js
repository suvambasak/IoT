var Gpio = require("onoff").Gpio;

// Initializing pin mode output (LEDs)
var led1 = new Gpio(12, 'out');
var led2 = new Gpio(25, 'out');
var led3 = new Gpio(23, 'out');
// Initializing pin mode input (Button).
var button = new Gpio(20, "in");

var counter = 0;
// Starting all LED status false : (OFF)
var ledStatus1 = false;
var ledStatus2 = false;
var ledStatus3 = false;
// All LEDs OFF.
led1.writeSync(0);
led2.writeSync(0);
led3.writeSync(0);

// Ready to start counting on click of button.
console.log("Ready...");
console.log("COUNTER : " + counter);


while (true) {
    // When button clicked.
    if (button.readSync() === 1) {
        console.log("BUTTON : CLICKED");
        counter++;

        // Reset when counter reaches to 7.
        if (ledStatus1 && ledStatus2 && ledStatus3) {
            ledStatus1 = false;
            ledStatus2 = false;
            ledStatus3 = false;
            led1.writeSync(ledStatus1);
            led2.writeSync(ledStatus2);
            led3.writeSync(ledStatus3);
            counter = 0;
            console.log("COUNTER : 0");
            continue;
        }

        console.log("COUNTER : " + counter);

        // LED 3 : (most significant bit)
        // Flip when LED 1 and LED 2 is HIGH.
        if (ledStatus1 && ledStatus2) {
            ledStatus3 = !ledStatus3;
            led3.writeSync(ledStatus3);
        }

        // LED 2
        // Flip when LED 1 is HIGH.
        if (ledStatus1) {
            ledStatus2 = !ledStatus2;
            led2.writeSync(ledStatus2);
        }

        // LED 1 : (least significant bit)
        // Flip on each click of button.
        if (ledStatus1) {
            ledStatus1 = false;
            led1.writeSync(ledStatus1);
        } else {
            ledStatus1 = true;
            led1.writeSync(ledStatus1);
        }

    }
}
