# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:17:18 2016

@author: albert
"""

class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.num_set = 0
        
class Game(object):
    def __init__(self, name_black, name_red, game_id):
        self.player_black = Player(name_black)
        self.player_red = Player(name_red)
        self.last_point_assigned_to = "none"
        self.current_set = 0        
        self.deuce = False   
        self.set_over = False
        self.game_over = False
        self.game_id = game_id
        self.result = None
        self.score = None

    def print_score(self):
        print("Score / %s %s - %s %s") % (self.player_black.name,self.player_black.score,self.player_red.score,self.player_red.name)

    def new_set(self):
        self.player_black.score = 0
        self.player_red.score = 0
        self.deuce = False
        self.current_set += 1
        self.set_over = False
        self.result = None
        self.score = None

    def judge(self):
        self.score = "The score is: " + self.player_black.name + " " + str(self.player_black.score)+ " and " + self.player_red.name + " " + str(self.player_red.score)
        if self.player_black.score==self.player_red.score and self.player_red.score >= 2 :
            self.deuce = True

        if not self.deuce:
            if self.player_black.score == 21:
                self.player_black.num_set += 1
                self.result = self.player_black.name+" Won Set "+str(self.current_set) 
                
                self.set_over = True

            if self.player_red.score == 21:
                self.player_red.num_set += 1
                self.result=self.player_red.name+" Won Set "+str(self.current_set)
                self.set_over = True

        elif self.deuce:
            if self.player_black.score == self.player_red.score:
                self.result="Deuce"

            elif self.player_black.score == self.player_red.score+1 or self.player_black.score == self.player_red.score-1:
                self.result = None
            elif self.player_black.score > self.player_red.score + 1:
                self.player_black.num_set += 1
                self.result=self.player_black.name+" Won Set "+str(self.current_set)
                self.set_over = True

            elif self.player_red.score > self.player_black.score + 1:
                self.player_red.num_set += 1
                self.result=self.player_red.name+" Won Set "+str(self.current_set)
                self.set_over = True

        if self.player_black.num_set == 2:
            self.game_over = True
            say_something (self.player_black.name+" Won "+str(self.player_black.num_set)+" Sets to "+str(self.player_red.num_set)+" against "+self.player_red.name)
            #update_score(player_black,player_red,self.player_black.num_set,self.player_red.num_set)
        if self.player_red.num_set == 2:
            self.game_over = True
            say_something (self.player_red.name+" Won "+str(self.player_red.num_set)+" Sets to "+str(self.player_black.num_set)+" against "+self.player_black.name)
            #update_score(player_red,player_black,self.player_red.num_set,self.player_black.num_set)

        