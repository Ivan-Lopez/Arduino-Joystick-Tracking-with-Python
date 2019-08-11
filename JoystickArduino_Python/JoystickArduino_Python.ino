const int xJoy=A7;
const int yJoy=A6;

int xVal=0;
int yVal=0;


void setup() {
  Serial.begin(9600);
  pinMode(xJoy, INPUT);
  pinMode(yJoy, INPUT);

}

void loop() {
  xVal=analogRead(xJoy);
  yVal=analogRead(yJoy);
  
  Serial.print(xVal);
  Serial.print(' ');
  Serial.println(yVal);
  delay(100);

}
