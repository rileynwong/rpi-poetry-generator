#!/usr/bin/env python
 
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
 
import RPi.GPIO as GPIO, time, os      
 
DEBUG = 1
GPIO.setmode(GPIO.BCM)
 
def get_light_intensity():
  RCpin = 16

  GPIO.setup(RCpin, GPIO.OUT)
  GPIO.output(RCpin, GPIO.LOW)

  time.sleep(0.1)
  GPIO.setup(RCpin, GPIO.IN)

  # This takes about 1 millisecond per loop cycle
  reading = 0
  while GPIO.input(RCpin) == GPIO.LOW:
    reading += 1

  return reading
 

### Main
if __name__ == "__main__":
	while True:
		light = get_light_intensity()
		print "light: ", light

