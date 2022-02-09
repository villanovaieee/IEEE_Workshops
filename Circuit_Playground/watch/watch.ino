// Copyright 2021 The Villanova Chapter of the Institute of Electrical and
// Electronics Engineers (IEEE)
// This file is part of the IEEE_Workshops library.
//
// The IEEE_Workshops libary is free software: you can redistribute it and/or
// modify it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or (at your
// option) any later version.
//
// The IEEE_Workshops libary is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
// Public License for more details.
//
// You should have received a copy of the GNU General Public License along with
// the IEEE_Workshops library. If not, see <https://www.gnu.org/licenses/>.

#include <Adafruit_CircuitPlayground.h>

uint8_t pixelh = 13;
uint8_t pixelm = 0;
uint32_t colorh = CircuitPlayground.colorWheel(60);
uint32_t colorm = CircuitPlayground.colorWheel(255);
uint32_t prevTime = 0;
uint8_t alarmh = 12;
uint8_t alarmm = 0;

uint8_t watchState = 0; // 0 watch, 1 set time
uint8_t alarmState = 0; // 0 off, 1 on, 2 deactivated

void setup()
{
  Serial.begin(9600);
  CircuitPlayground.begin();
  CircuitPlayground.speaker.enable(true);
}

void loop()
{
  if (CircuitPlayground.leftButton() && !watchState)
  {
    while (CircuitPlayground.leftButton())
      ; // wait for button release
    watchState = 1;
  }
  if (CircuitPlayground.rightButton() && !watchState)
  {
    while (CircuitPlayground.rightButton())
      ;
    watchState = 2;
  }
  if (alarmState != 2)
    alarmState = CircuitPlayground.slideSwitch();

  switch (watchState)
  {
  case 0:
    updateTime();
    displayHour(&pixelh);
    displayMinute(&pixelm);
    break;
  case 1:
    setTime(1);
    break;
  case 2:
    setTime(0);
    break;
  }
}

void updateTime()
{
  uint32_t deltat = millis() - prevTime;
  if (deltat >= 60000)
  {
    ++pixelm;
    prevTime = millis() + deltat - 60000;
    CircuitPlayground.clearPixels();
    CircuitPlayground.redLED(LOW);
  }
  if (pixelm > 59)
  {
    ++pixelh;
    pixelm = 0;
  }
  if (pixelh == alarmh && pixelm == alarmm && alarmState == 1)
  {
    alarm();
  }
  if (pixelh == alarmh + 1 || pixelm == alarmm + 1 && alarmState == 2)
  {
    alarmState = CircuitPlayground.slideSwitch();
  }
}

void displayHour(uint8_t *p)
{
  if (*p & (1 << 0))
    CircuitPlayground.setPixelColor(0, colorh);
  if (*p & (1 << 1))
    CircuitPlayground.setPixelColor(1, colorh);
  if (*p & (1 << 2))
    CircuitPlayground.setPixelColor(2, colorh);
  if (*p & (1 << 3))
    CircuitPlayground.setPixelColor(3, colorh);
  if (*p & (1 << 4))
    CircuitPlayground.setPixelColor(4, colorh);
}

void displayMinute(uint8_t *p)
{
  CircuitPlayground.redLED(*p & (1 << 0));
  if (*p & (1 << 1))
    CircuitPlayground.setPixelColor(9, colorm);
  if (*p & (1 << 2))
    CircuitPlayground.setPixelColor(8, colorm);
  if (*p & (1 << 3))
    CircuitPlayground.setPixelColor(7, colorm);
  if (*p & (1 << 4))
    CircuitPlayground.setPixelColor(6, colorm);
  if (*p & (1 << 5))
    CircuitPlayground.setPixelColor(5, colorm);
}

void setTime(uint8_t t)
{
  if (t)
  {
    changeHour(&pixelh);
    changeMinute(&pixelm);
  }
  else
  {
    changeHour(&alarmh);
    changeMinute(&alarmm);
  }

  watchState = 0;
}

void changeHour(uint8_t *p)
{
  while (!CircuitPlayground.leftButton())
  { // wait for button press
    displayHour(p);
    delay(500);
    CircuitPlayground.clearPixels();
    delay(500);

    if (CircuitPlayground.rightButton())
    {
      if (*p == 23)
        *p = 0;
      else
        ++*p;
      while (CircuitPlayground.rightButton())
        ;
    }
  }
  while (CircuitPlayground.leftButton())
    ;
}

void changeMinute(uint8_t *p)
{
  while (CircuitPlayground.leftButton())
    ; // wait for button release
  while (!CircuitPlayground.leftButton())
  { // wait for button press
    displayMinute(p);
    delay(500);
    CircuitPlayground.clearPixels();
    CircuitPlayground.redLED(LOW);
    delay(500);

    if (CircuitPlayground.rightButton())
    {
      if (*p == 60)
        *p = 0;
      else
        ++*p;
      while (CircuitPlayground.rightButton())
        ;
    }
  }
  while (CircuitPlayground.leftButton())
    ;
}

void alarm()
{
  uint32_t aStart = millis();
  alarmState = 2;
  while (!CircuitPlayground.leftButton() && (millis() - aStart) < 60000 && CircuitPlayground.slideSwitch())
  {
    CircuitPlayground.playTone(10000, 300, true);
  }
  while (CircuitPlayground.leftButton() && (millis() - aStart) < 60000 && CircuitPlayground.slideSwitch())
    ; // need time check here too in case time runs out
}
