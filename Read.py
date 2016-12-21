#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = None
MIFAREReader = None

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

def initialize():
    global continue_reading, MIFAREReader
    continue_reading = True

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

def get_user_by_rfid(uuid):
    if uuid == "108928475":
        return "P1"
    elif uuid == "367191236":
        return "P2"


def main():
    global continue_reading, MIFAREReader
    # Welcome message

    print "Running RFID reader to identify user"
    print "Press Ctrl-C to stop."

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:

        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status is MIFAREReader.MI_OK:
            print "Card detected"

            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status is MIFAREReader.MI_OK:

                # Build full uid
                fulluid = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])

                # Print UID
                print "Card read UID: "+ fulluid

                # Get user by rfid from the users db
                found_user = get_user_by_rfid(fulluid)

                if (found_user):
                    print "Found user : " + str(found_user)

                    # Sleep for a but so that we don't double up on the same user
                    time.sleep(10)

if __name__ == '__main__':
    initialize()
    main()
