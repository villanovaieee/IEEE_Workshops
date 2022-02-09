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

const uint8_t nSamples = 20;
uint8_t threshold = 400;

uint16_t samples[nSamples];
uint16_t dc_minimum = 1024;
uint16_t reading = 0;

uint32_t pulseOneTime = 0;
uint32_t pulseTwoTime = 0;
uint32_t pulseInterval = 0;

float BPM = 0;

bool ignoreReading = false;
bool pulseOneDetected = false;

void setup()
{
  Serial.begin(115200);
  CircuitPlayground.begin();
  CircuitPlayground.setPixelColor(1, 0, 255, 0);
}

void loop()
{

  for (int i = 0; i < nSamples; i++)
  {
    samples[i] = CircuitPlayground.lightSensor();

    dc_minimum = 1024;
    for (int j = 0; j < nSamples; j++)
    {
      dc_minimum = min(dc_minimum, samples[j]);
    }

    //    CircuitPlayground.setPixelColor(5, samples[i] - dc_minimum, 0, 0);

    reading = samples[i] - dc_minimum;
    if (reading > threshold && !ignoreReading)
    {
      if (!pulseOneDetected)
      {
        pulseOneDetected = true;
        pulseOneTime = millis();
      }
      else
      {
        pulseTwoTime = millis();
        pulseInterval = pulseTwoTime - pulseOneTime;
        pulseOneTime = pulseTwoTime;
      }
      ignoreReading = false;
    }

    if (reading < threshold)
    {
      ignoreReading = false;
    }

    BPM = (1.0 / pulseInterval) * 60000.0;

    Serial.print(reading);
    Serial.print("\t");
    Serial.print(pulseInterval);
    Serial.print("\t");
    Serial.print(BPM);
    Serial.println(" BPM");
    Serial.flush();

    //    Serial.println(samples[i] - dc_minimum);
    //    if(samples[i] - dc_minimum > threshold) {
    //      CircuitPlayground.setPixelColor(4, 255, 0, 0);
    //    } else {
    //      CircuitPlayground.setPixelColor(4, 0, 0, 0);
    //    }
    delay(50);
  }
}
