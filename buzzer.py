
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
buzzer = 18
ON = False
OFF = True
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.HIGH)
for c in range(0,10): # Run forever
    GPIO.output(buzzer, GPIO.LOW) # Turn on
    print("green")
    sleep(0.7) # Sleep for 1 second
    GPIO.output(buzzer, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    GPIO.output(buzzer, ON) # Turn on
    print("yellow")
    sleep(0.1) # Sleep for 1 second
    GPIO.output(buzzer, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    GPIO.output(buzzer, GPIO.HIGH) # Turn on
    print("red")
    sleep(1.5) # Sleep for 1 second
    GPIO.output(buzzer, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    GPIO.output(buzzer, ON) # Turn on
    print("white")
    sleep(0.5) # Sleep for 1 second
    GPIO.output(buzzer, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    
GPIO.cleanup()
 




# Set #18 as buzzer pin
BuzzerPin = 18
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set BuzzerPin's mode to output, 
    # and initial level to High(3.3v)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.HIGH)

def main():
    print_message()
    while True:
      GPIO.output(BuzzerPin, GPIO.LOW)
      time.sleep(0.3)
      GPIO.output(BuzzerPin, GPIO.HIGH)
      time.sleep(0.3)