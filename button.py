import RPi.GPIO as GPIO
import pygame


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit\n\n")

GPIO.cleanup()

def button_callback(channel):
    print()
    print("Button was pushed")


pygame.mixer.init()
pygame.mixer.music.load("thevalkyrie.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
