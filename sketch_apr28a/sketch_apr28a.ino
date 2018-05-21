const int CO2Pin = A0;
const int LDRPin = A1;
const int constant1 = 1
const int constant2 = 1

void setup(){
  Serial.begin(9600);
  pinMode(CO2Pin, INPUT)
  pinMode(LDRPin, INPUT)
}
void loop(){
  CO2Concentration = analogRead(CO2Pin)/constant2
  LightIntensity = analogRead(LDRPin)/consant1
  myArray[2] = {CO2Concentration, LightIntensity}
  sendData(myArray, 2);
  delay(1000);
}

void sendData (int dataArray[], int lenght) {
  for(int n=0; n < lenght; n++){
    if(n==0){
      Serial.print(dataArray[n]);
      Serial.print(" => ");
    }
    else if (n == (lenght -1)){
      Serial.println(dataArray[n]);
    }
    else {
      Serial.print(dataArray[n]);
      Serial.print(" => ");
    }
  }
}
