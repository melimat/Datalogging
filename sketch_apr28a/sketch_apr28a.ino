int a = 0;
void setup(){
  Serial.begin(9600);
}
void loop(){
  a ++;
  Serial.println(a);
  delay(10);
}
