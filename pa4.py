#Programmer: Katie Beattie
#Course: CS121; Dr. Rajeev
#Programming Assignment: 4

#random module to shuffle the cards
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#decides if player is playing or not
playing = True

#begins the card class
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

#creates the deck class
class Deck:

#start with an empty list
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#creates Hand class
class Hand:

#start with an empty list again
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -+ self.bet

#taking bets
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed '.format(chips.total))
            else:
                break

#if the player decides to take hits or stand
def hit_or_stand(deck,hand):
   global playing

   while True:
       x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

       if x[0].lower() == 'h':
           hit(deck, hand)

       elif x[0].lower() == 's':
           print("Player stands. Dealer is playing.")
           playing = False

       else:
           print("Sorry, please try again.")
           continue
       break

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

#possible game scenarios
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

#code for the game itself;
while True:
    #opening statement
    print("Welcome to Blackjack.")

    # create and shuffle deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set player's chips
    player_chips = Chips()

    # prompt player for their bet
    take_bet(player_chips)

    # show cards NOTE: keep one dealer card hidden
    show_some(player_hand, dealer_hand)

    while playing:

        # prompt for player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # show cards  NOTE: keep one dealer card hidden
        show_some(player_hand,dealer_hand)

        # if player's hand value is greater than 21, run player_busts() and break out of loop
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If the player hasn't busted, algorithm should play the dealer's hand until 17
    if player_hand.value <= 21:

        while dealer_hand.value <17:
            hit(deck, dealer_hand)

        # show all cards
        show_all(player_hand,dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)


    # output chips total to player
    print("\nPlayers winnings stand at", player_chips.total)

    # ask user to play again
    play_again = input("would you like to play again? Enter yes or no: ")
    if play_again[0].lower() == 'yes':
        playing = True
        continue
    else:
      print("Thanks for playing!")
