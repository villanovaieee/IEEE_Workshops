
#include <Adafruit_CircuitPlayground.h>

uint8_t pixelh = 7;
uint8_t pixelm = 2;
uint8_t colorh = 255;
uint8_t colorm = 60;

uint8_t watchState = 0; // 0 watch, 1 set time

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
}

void loop() {
  if (CircuitPlayground.leftButton() && !watchState) {
    watchState = 1;
  }

  switch(watchState) {
    case 0:
      CircuitPlayground.setPixelColor(pixelh, CircuitPlayground.colorWheel(colorh));
      CircuitPlayground.setPixelColor(pixelm, CircuitPlayground.colorWheel(colorm));
      break;
    case 1:
      setTime();
      break;
  }
}

void setTime() {
  changePixel(&pixelh, colorh);
  changePixel(&pixelm, colorm);  

  watchState = 0;
}

void changePixel(uint8_t* p, uint8_t c) {
  while(CircuitPlayground.leftButton()); // wait for button release
  while(!CircuitPlayground.leftButton()) { //wait for button press
    CircuitPlayground.setPixelColor(*p, CircuitPlayground.colorWheel(c));
    delay(500);
    CircuitPlayground.clearPixels();
    delay(500);

    if(CircuitPlayground.rightButton()) {
      Serial.print("Previous pixel: ");
      Serial.print(*p);
      Serial.print(" Current Pixel: ");
      if(*p == 0) *p = 9;
      else *p--;
      Serial.println(*p);
      while(CircuitPlayground.rightButton());
    }
  }
  while(CircuitPlayground.leftButton());
}
