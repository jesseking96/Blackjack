from random import randint

class Deck():
    
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    face_cards = ["King", "Queen", "Jack", "Ace"]
    
    def __init__(self):
        '''
        Initially populates the deck
        '''
        self.contents = []
        for suit in self.suits:
            for num in range(2,11):
                self.contents.append((num, suit))
            for face_card in self.face_cards:
                self.contents.append((face_card, suit))
    
    def reset(self):
        '''
        Resets the contents of the deck
        '''
        self.contents = []
        for suit in self.suits:
            for num in range(2,11):
                self.contents.append((num, suit))
            for face_card in self.face_cards:
                self.contents.append((face_card, suit))

    def deal_card(self):
        '''
        Randomly selects a card from the deck
        removes card from the deck, then returns the card
        '''
        card = self.contents[randint(0,len(self.contents) - 1)]
        self.contents.remove(card)
        return card
        
class Player():
    
    def __init__(self, name, balance = 200):
        '''
        assigns the name of the player and initial balance
        '''
        self.name = name
        self.balance = balance
    
    def __str__(self):
        return "Name : {} \nBalance: ${}".format(self.name,self.balance)
    
    def welcome_player(self):
        '''
        Welcomes the player to the game
        '''
        print(f"\nWelcome {self.name}!")
    
    def bet_amount(self):
        '''
        prompts the user to place a bet.
        checks if the player has enough money to bet.
        '''
        while True:
            try:
                print(f"\nBalance: ${self.balance}")
                self.bet = int(input('How much would you like to bet? '))
            except ValueError:
                print("Invalid input. Try again.")
                continue
            if self.bet > self.balance:
                print("\nYou don't have enough money! Try again.")
                continue
            elif self.bet <= 0:
                print("Invalid input. Try again.")
                continue
            elif self.bet > 500:
                print("\nBets are limited to $500. Try again.")
                continue
                
            break
    
    def win(self):
        '''
        adds the amount of the player's bet to the player's balance
        '''
        self.balance += (self.bet)
    
    def lose(self):
        '''
        subtracts the player's bet from the player's balance
        '''
        self.balance -= self.bet
        
class Hand():
    
    def __init__(self, owner):
        self.owner = owner
        self.cards = []
        self.total = 0
    
    def new_hand(self, new_card1, new_card2):
        '''
        empties the current hand, and assigns a new hand
        new cards should be pulled from Deck
        '''
        self.cards = []
        self.total = 0
        self.cards.append(new_card1)
        self.cards.append(new_card2)
    
    def is_hit(self):
        '''
        prompts the player to hit or stand
        checks for a valid response
        '''
        while True:
            choice = input("Would you like to hit or stand(H/S)? ")
            if choice.upper() == "H":
                return True
            elif choice.upper() == "S":
                return False
            else:
                print("Invalid input. Try again.")
    
    def hit(self, new_card):
        '''
        adds a new card to hand
        new card should be pulled from deck
        '''
        self.cards.append(new_card)
    
    def is_bust(self):
        '''
        checks if the player/dealer has busted, and returns the boolean result
        '''
        return self.total > 21
    
    def card_value(self, card):
        '''
        translates the card into a value to be added.
        Aces are assumed to equal 11 by default. Aces are converted to equal
        1 when necessary elsewhere
        '''
        if card[0] in range(2,11):
            card_value = card[0]
        elif card[0] in ["King", "Queen", "Jack"]:
            card_value = 10
        elif card[0] == "Ace":
            card_value = 11
        return card_value
    
    def update_total(self):
        '''
        Updates the total value of the cards in the hand
        '''
        self.total = 0
        for card in self.cards:
            if self.card_value(card) in range(2,12):
                self.total += self.card_value(card)
        for (card, rank) in self.cards:
            if self.total > 21:
                if card == "Ace":
                        self.total -= 10
            else:
                break
    
    def print_hand(self):
        '''
        Prints the player or dealers hand and total
        '''
        print(f"\n{self.owner}'s hand includes:\n")
        for (card, suit) in self.cards:
            print(f"{card} of {suit}\n")
        print(f"Total: {self.total}")
        
    def print_dealers_card(self):
        '''
        prints the dealers first card, which would be visible to the player
        at the beginning of the hand
        '''
        print(f"\n\nDealer's card is {self.cards[0][0]} of {self.cards[0][1]}\n")
        
class Game():
    
    def __init__(self):
        '''
        initializes play_game to true
        '''
        self.play_game = True
    
    
    def print_intro(self):
        '''
        Prints the introduction to the game, explaining the rules
        '''
        
        print('''
        -----------------------------------------------------------------------      
        
        ***   *          *      *****   *  *    * * * *     *      *****   *  *
        *  *  *         * *    *        * *        *       * *    *        * *  
        ***   *        *****   *        **         *      *****   *        **   
        *  *  *       *     *  *        * *    *   *     *     *  *        * *  
        ***   ******  *     *   *****   *  *    * *      *     *   *****   *  *
              
        -----------------------------------------------------------------------
        ''')
        print("\n\nWelcome to Blackjack!")
        print("The goal of the game is to get the sum of your cards")
        print("as close to 21 as possible, without exceeding 21.")
        print("If you exceed 21, you bust and lose the hand.")
        print("If the dealer gets closer to 21 than you, without busting,")
        print("then the dealer wins. To win, you'll have to beat the dealer.")
        print("Kings, Queens, and Jacks are worth 10.")
        print("Aces can be worth 1 or 11, whichever is advantageous to you.")
        print("Bets are limited to $500\n\n")
        
    def get_player(self):
        '''
        Prompts the player for their name, and returns the results
        '''
        name = input("What is your name? ")
        return name
    
    
    def is_tie(self, player_total, dealer_total):
        '''
        checks if the game ended in a tie, and returns the boolean result
        '''
        return player_total == dealer_total == 21
    
    def is_win(self, player_total, dealer_total):
        '''
        checks if the player has beat the dealer, and returns the boolean result
        '''
        return player_total > dealer_total
        
    def play_again(self):
        '''
        prompts the player to play another hand
        checks for valid input
        '''
        while True:
            replay = input("Would you like to play another hand(Y/N)? ")
            if replay.upper() == "Y":
                break
            if replay.upper() == "N":
                self.play_game = False
                break
            else:
                print("Invalid input. Try again.")
        
    def check_game_over(self, balance):
        if balance <= 0:
            self.play_game = False
            print("\nYou're out of money!")
        
    def outro(self, name, balance):
        print(f"\nThanks for playing {name}!")
        print(f"\nYour final balance was ${balance}.")
        
    
