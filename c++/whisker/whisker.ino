#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int PIN_left = 5;
int LEDPIN = 4;
int PIN_right = 7;
int i = 0;

bool hitonce = false;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(LEDPIN, OUTPUT);
  pinMode(PIN_left, INPUT);
  pinMode(PIN_right, INPUT);
  servoLeft.attach(12);
  servoRight.attach(13);
}
void ForwardServos()
{
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
}

void BackwardServos() 
{
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);  
}

void LeftServos() 
{
  servoLeft.writeMicroseconds(1300);  
  servoRight.writeMicroseconds(1300);  
}

void RightServos()
{
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1700);
}

void hitright()
{
  
  if (digitalRead(7) == HIGH)
  {
    digitalWrite(4, LOW);
    ForwardServos();
  }
  
  else
  { 
    hitonce = true;
    digitalWrite(4, HIGH);
    BackwardServos();
    delay(500);
    LeftServos();
    delay(500);
  }
}

void hitleft()
{
  if (digitalRead(5) == HIGH)
  {
    digitalWrite(4, LOW);
    ForwardServos();
  }
  
  else
  { 
    if(hitonce == true);
    {
      i++;
      hitonce = false;
    }
    digitalWrite(4, HIGH);
    BackwardServos();
    delay(500);
    RightServos();
    delay(300);
  }
}

void check()
{
  if(i == 5)
  {
    hitleft();
    int i = 0;
  }
  
}

void loop()
{
  hitright();
  hitleft();
  check();
}


