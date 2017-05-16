// https://bitbucket.org/fmalpartida/new-liquidcrystal/downloads <- Biblioteka pod I2C

#include <LiquidCrystal_I2C.h>
#include <Wire.h>
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

void setup() {
 lcd.begin(16,2);
 Serial.begin(9600);
}

void loop() {
 if (Serial.available()) {
  lcd.clear();
  while ( !Serial.available());
   lcd.print(Serial.readString());
}
}
