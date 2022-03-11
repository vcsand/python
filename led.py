from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO_BOARD
GPIO.setup(23,GPIO.OUT,initial=GPIO.LOW)
#inicializalas
while True:
	GPIO.output(23, GPIO.HIGH)
	sleep(0.1)
	GPIO.output(23, GPIO.LOW)
	sleep(0.1)

