int myArray[7] = {
  0, 1, 2, 3, 4, 5, 6} 
;
void setup(){
  Serial.begin(9600);
}
void loop(){
  sendData(myArray, 7);
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

