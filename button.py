import RPi.GPIO as GPIO
import pygame
import schedule
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init()
pygame.mixer.music.load("thevalkyrie.mp3")

def alarm(t):
    print("alarm triggered")

    pygame.mixer.music.play()

    def button_callback(channel):
        print("Button was pushed")
        pygame.mixer.music.stop()

    GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

    message = input("Press enter to quit\n\n")

    GPIO.cleanup()

schedule.every().day.at("21:00").do(alarm,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
