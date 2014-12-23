#include "Final_Code.h"

//init the ADC pins
int PulseOximeter_ADC = A1;
int Temperature_ADC = A0;

//function to write the data packet to the serial port
//header consists of 0xFFFF
void WritePacket(void){
  Serial.write(highByte(PacketHeader));
  Serial.write(lowByte(PacketHeader));

  //get temperature reading from ADC and write the 10bit value
  //split into two bytes
  int temperature = analogRead(Temperature_ADC);
  Serial.write(highByte(temperature));
  Serial.write(lowByte(temperature));
  
  int pulse_oximiter = analogRead(PulseOximeter_ADC);
  Serial.write(highByte(pulse_oximiter));
  Serial.write(lowByte(pulse_oximiter));    
}

//init the Arduino
void setup() {
  pinMode(Temperature_ADC, INPUT);
  pinMode(PulseOximeter_ADC, INPUT);
  pinMode(13,OUTPUT);
  
  Serial.begin(9600);
}

//main loop - flash LEDs with 10ms period
//write data packet every 20ms
void loop() {
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(10);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(10);              // wait for a second

  WritePacket();
}
