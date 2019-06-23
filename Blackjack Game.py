#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:30:58 2019

@author: skyking
"""

import Blackjack as B

   
game = B.Game()
deck = B.Deck()
game.print_intro()
name = game.get_player()
player = B.Player(name)
player_hand = B.Hand(name)
dealer = B.Player("Dealer")
dealer_hand = B.Hand("Dealer")
player.welcome_player()

while game.play_game:
    deck.reset()
    player.bet_amount()
    player_hand.new_hand(deck.deal_card(), deck.deal_card())
    dealer_hand.new_hand(deck.deal_card(), deck.deal_card())
    player_hand.update_total()
    dealer_hand.update_total()
    dealer_hand.print_dealers_card()
    player_hand.print_hand()
    
    player_busted = False
    while player_hand.is_hit():
        
        player_hand.hit(deck.deal_card())
        player_hand.update_total()
        if player_hand.is_bust():
            player_hand.print_hand()
            print("\nYou've busted!")
            player_busted = True
            player.lose()
            break
        
        player_hand.print_hand()
    if player_busted == True:
        continue
    dealer_hand.update_total()
    
    while (not dealer_hand.is_bust()) and dealer_hand.total <= player_hand.total:
        if game.is_tie(player_hand.total, dealer_hand.total):
            dealer_hand.print_hand()
            print("\nTie!")
            break
        dealer_hand.hit(deck.deal_card())
        dealer_hand.update_total()
        
    
    if dealer_hand.is_bust():
        print("\nDealer busted, you win!")
        player.win()
    elif game.is_win(player_hand.total, dealer_hand.total):
        dealer_hand.print_hand()
        print("\nYou win!")
        player.win()
    else:
        dealer_hand.print_hand()
        print("\nYou lose!")
        player.lose()