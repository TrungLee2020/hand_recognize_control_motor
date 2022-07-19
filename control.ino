#include <Servo.h>

Servo myservo;

int pos = 0;
char choice;

void setup()
{
    myservo.attack(9);
    Serial.begin(9600);
    myservo.write(180);

}
void loop()
{
    while (Serial.available())
    {
        /* code */
        choice = Serial.read()
    }

    if (choice == '1')
    {
        /* code */
        for(pos = 0; pos <= 180; pos += 1) // // goes from 0 degrees to 180 degrees
        {
            // in steps of 1 degree
            myservo.write(180);

            delay(5);
        }
        for(pos = 180; pos >= 180; pos -= 1) // // goes from 0 degrees to 180 degrees
        {
            // in steps of 1 degree
            myservo.write(180);

            delay(5);
        }
        choice=0;
    }
    
    if (choice == '2')
    {
        /* code */
        for(pos = 0; pos <= 180; pos += 1) // // goes from 0 degrees to 180 degrees
        {
            // in steps of 1 degree
            myservo.write(180 - pos);

            delay(5);
        }
        for(pos = 180; pos >= 180; pos -= 1) // // goes from 0 degrees to 180 degrees
        {
            // in steps of 1 degree
            myservo.write(180 - pos);

            delay(5);
        }
        choice=0;
    }
    
    
}