
#include <Adafruit_CircuitPlayground.h>

float soundLevel;
float mean;
float clapSens = 30;

uint8_t clapState = 0;
uint8_t active = 0;
uint32_t samples = 100;
uint32_t minDeltaMs = 250; // minimum time to pass before next clap
uint32_t maxDeltaMs = 1000; // maximum time to pass before reset
uint32_t clapOneTime = 0;
uint32_t clapTwoTime = 0;

void setup() {
  uint32_t i = 0;
  float oversample = 0.0;
  Serial.begin(9600);
  CircuitPlayground.begin();
  delay(100);
  for(i=0; i<samples; i++) {
    oversample += CircuitPlayground.mic.soundPressureLevel(5);
  }
  mean = oversample / samples;
  Serial.print("Mean sample: "); Serial.println(mean);
}

void loop() {
  // measures the acutal pressure level which is great for measuring "spikes" in sound
  // we will test for two spikes

  soundLevel = CircuitPlayground.mic.soundPressureLevel(5);

  if(soundLevel - mean > clapSens && !clapState) {
    clapState = 1;
    while(CircuitPlayground.mic.soundPressureLevel(5) > mean + clapSens); // wait for clap to dissipate
    clapOneTime = millis();
    Serial.print("Clap One: "); Serial.println(soundLevel);
  }
  else if(soundLevel - mean > clapSens && clapState == 1) {
    // second clap
    clapTwoTime = millis();
    clapState = 2;
    while(CircuitPlayground.mic.soundPressureLevel(5) > mean + clapSens); // wait for clap to dissipate
    
    if (clapTwoTime - clapOneTime < minDeltaMs) {
      Serial.println("Too fast!");
      clapState = 0;
    }
    else {
      active = !active;
      clapState = 0;
    }
  }
  else if (millis() - clapOneTime > maxDeltaMs && clapState == 1) {
    Serial.println("Too slow!");
    clapState = 0;
  }

  if(active) {
    // claps worked
    for (int i =0; i<10; i++) {
      CircuitPlayground.setPixelColor(i, CircuitPlayground.colorWheel(255));
    }
  }
  else {
    CircuitPlayground.clearPixels();
  }
}
