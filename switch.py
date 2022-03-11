from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO_BOARD
GPIO.setup(23,GPIO.IN)
#inicializalas
elozo = 0
while True:
	bemenet = GPIO.input(23)
	if (not elozo and bemenet):
		print("Gomb benyomva!")
	elozo = bemenet
	sleep(0.5)

