import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# return distance in cm
def get_distance():
	GPIO.output(TRIG, False)
	time.sleep(2)


	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150 # convert to cm
	distance = round(distance, 2)

	return distance


### Main
if __name__ == "__main__":
	while True:
		distance = get_distance()
		print "Distance:",distance,"cm"

