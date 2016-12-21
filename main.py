from makeAthing import *
import random
from updatescore import update_score
from random import randint
from pingpongbot import *
import RPi.GPIO as GPIO
import MFRC522
import signal
import time
from subprocess import Popen, PIPE

def say_something(something):
        p1 = Popen(["echo", something], stdout=PIPE)
        p2 = Popen(["festival", "--tts"], stdin=p1.stdout, stdout=PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        output = p2.communicate()[0]

def get_user_by_rfid(uuid):
    if uuid == "108928475":
        return "Brandon"
    elif uuid == "367191236":
        return "Shawn"

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

readingPlayer = True
MIFAREReader = None
player_red = None
player_black = None


pong_hardware_init()




signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()
running = True
saidDeuce = False

while running:
	say_something("Waiting for players")
	while readingPlayer:
		if get_big_btn_press():
			player_red = None
			player_black = None	
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

	            if player_red == None:
	                player_red = get_user_by_rfid(fulluid)
	                say_something(player_red+"Log in")
	            elif(player_red != get_user_by_rfid(fulluid)):
	                player_black = get_user_by_rfid(fulluid)
	                say_something(player_black+"Log in")

	            # Sleep for a but so that we don't double up on the same user
	            time.sleep(2)
	            if(player_black and player_red):
	            	readingPlayer=False

	say_something("Game Start. "+player_red+" versus "+player_black)
	new_game = Game(player_black,player_red,random.randint(1,1000))
	new_game.new_set()
	while not new_game.game_over:
		if get_big_btn_press():
			player_red = None
			player_black = None	
			readingPlayer = True
			new_game.game_over = True
		if get_reddn_btn_press() or get_blackdn_btn_press():
			if new_game.last_point_assigned_to == "none":
				say_something("Undo Unable")	
			if new_game.last_point_assigned_to == "b":
				new_game.player_black.score -= 1
				new_game.print_score()
				new_game.judge()
				say_something(new_game.score)
				if(new_game.result):
					say_something(new_game.result)
				new_game.last_point_assigned_to ="none"
			if new_game.last_point_assigned_to == "r":
				new_game.player_red.score -= 1
				new_game.print_score()
				new_game.judge()
				say_something(new_game.score)
				if(new_game.result):
					say_something(new_game.result)
				new_game.last_point_assigned_to = "none"

		if get_blackup_btn_press():
			new_game.player_black.score += 1
			new_game.last_point_assigned_to = "b"
			new_game.print_score()
			new_game.judge()
			say_something(new_game.score)
			if(new_game.result):
				say_something(new_game.result)

		if get_redup_btn_press():
			new_game.player_red.score += 1
			new_game.last_point_assigned_to = "r"
			new_game.print_score()
			new_game.judge()
			say_something(new_game.score)
			if(new_game.result):
				say_something(new_game.result)

		if self.player_black.num_set == 2:
            self.game_over = True
            say_something (self.player_black.name+" Won "+str(self.player_black.num_set)+" Sets to "+str(self.player_red.num_set)+" against "+self.player_red.name)
            #update_score(player_black,player_red,self.player_black.num_set,self.player_red.num_set)
        if self.player_red.num_set == 2:
            self.game_over = True
            say_something (self.player_red.name+" Won "+str(self.player_red.num_set)+" Sets to "+str(self.player_black.num_set)+" against "+self.player_black.name)
            #update_score(player_red,player_black,self.player_red.num_set,self.player_black.num_set)

        if not self.game_over:
            if self.set_over:
                say_something("New Set")
                self.new_set()
		#else:
		#	if not new_game.deuce:
		#		if ((new_game.player_black.score + new_game.player_red.score) % 5) == 0 and new_game.last_point_assigned_to != "none":
		#			print("dd Switch Serve")
		#	else:
		#		print("Switch Serve")

