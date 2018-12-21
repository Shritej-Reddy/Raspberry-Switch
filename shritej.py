import requests as req
import RPi.GPIO as GPIO

from time import sleep

pin = 23
pinled = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinled, GPIO.OUT)
input_state = True


while True:
    input_state = GPIO.input(pin)
    if input_state == False:
        data = req.get("http://13.127.46.61/api/show.php")
        value = data.text

        if value == "on":
            value = "off"

        elif value == "off":
            value = "on"

        payload = {"button" : value}
        stat = req.get("http://13.127.46.61/api/button.php", params = payload)
        sleep(0.2)

    data = req.get("http://13.127.46.61/api/show.php")
    value = data.text
    if value == "on":
        GPIO.output(pinled, GPIO.HIGH)
    elif value == "off":
        GPIO.output(pinled, GPIO.LOW)
