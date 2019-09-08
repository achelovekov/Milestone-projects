import random
from IPython.display import clear_output

class BasePlayer():
    '''
    Attributes:
        - name - name of the player
        - hand - cards from the deck 
    '''
    def __init__(self, name, hand={}):
        self.name = name
        self.hand = hand
        
    def __str__(self):
        return f"Player name: {self.name}\nPlayer hand: {self.hand}"

    def hit(self, deck):
        card = random.choice(list(deck.items()))
        deck.pop(card[0])

        self.hand[card[0]]=card[1]

    def stay(self):
        return True

class Dealer(BasePlayer):
    
    def __init__(self, name, hand={}):
        BasePlayer.__init__(self,name, hand={})


class Player(BasePlayer):
    
    def __init__(self, name, stack, hand={}):
        BasePlayer.__init__(self, name, hand={})
        self.stack = stack
    
    def __str__(self):
        return f"Player name: {self.name}\nPlayer hand: {self.hand}\nPlayer stack: {self.stack}"

class Game():

    def __init__(self):
        self.dealer = Dealer('dealer')
        self.player = Player('player',stack=100)

class Round():
    '''
    ask for bet
    ask for hit/stay
    check value for > 21
    '''
    def __init__(self,dealer,player):
        self.player = player
        self.dealer = dealer
        self.deck = {
            '2-D' : 2,
            '3-D' : 3,
            '4-D' : 4,
            '5-D' : 5,
            '6-D' : 6,
            '7-D' : 7,
            '8-D' : 8,
            '9-D' : 9,
            '10-D': 10,
            '2-H' : 2,
            '3-H' : 3,
            '4-H' : 4,
            '5-H' : 5,
            '6-H' : 6,
            '7-H' : 7,
            '8-H' : 8,
            '9-H' : 9,
            '10-H': 10,
            '2-S' : 2,
            '3-S' : 3,
            '4-S' : 4,
            '5-S' : 5,
            '6-S' : 6,
            '7-S' : 7,
            '8-S' : 8,
            '9-S' : 9,
            '10-S': 10,
            '2-C' : 2,
            '3-C' : 3,
            '4-C' : 4,
            '5-C' : 5,
            '6-C' : 6,
            '7-C' : 7,
            '8-C' : 8,
            '9-C' : 9,
            '10-C': 10,
            'J-D' : 10,
            'Q-D' : 10,
            'K-D' : 10,
            'J-H' : 10,
            'Q-H' : 10,
            'K-H' : 10,
            'J-S' : 10,
            'Q-S' : 10,
            'K-S' : 10,
            'J-C' : 10,
            'Q-C' : 10,
            'K-C' : 10,
            'A-D' : 11,
            'A-H' : 11,
            'A-S' : 11,
            'A-C' : 11
        }
        self.player_bet = 0

        for i in range(2): dealer.hit(self.deck)
        for i in range(2): player.hit(self.deck)

    def ask_for_bet(self):
        while True:
            try:
                while True:
                    player_bet = int(input("Enter your bet: "))
                    if player_bet > self.player.stack:
                        print("You do not have enough stack!")
                    else:
                        self.player_bet = player_bet
                        break
            except:
                print("Enter int value")
                continue
            else:
                break

    def ask_for_turn(self):

        while True:
            turn = input("Do you wish to hit/stay?: ")
            if turn == 'hit':
                self.player.hit(self.deck)
                return True
            elif turn == 'stay':
                return False
            else:
                print("Enter hit or stay!")

    def player_play(self):
        #return - stop the game - False
        #         continue with dealer - True 
        while sum(self.player.hand.values()) < 21:
            if self.ask_for_turn():
                self.round_print_player()
            else:
                return True

        if sum(self.player.hand.values()) == 21:
            self.player.stack += self.player_bet * 0.5
            self.round_hands_reset()

            print("Player has a blackjack!")
            return False

        elif sum(self.player.hand.values()) > 21:
            self.round_ace_transform(self.player)

            while sum(self.player.hand.values()) < 21:
                if self.ask_for_turn():
                    self.round_ace_transform(self.player)
                    self.round_print_player()
                else:
                    return True

            if sum(self.player.hand.values()) > 21:
                self.player.stack -= self.player_bet
                self.round_hands_reset()

                print("Player busts!")
                return False

            elif sum(self.player.hand.values()) == 21:
                self.round_hands_reset()

                print("Player has a blackjack!")
                return False

    def dealer_play(self):
        while sum(self.dealer.hand.values()) < 17:
            self.dealer.hit(self.deck)
            
        if sum(self.dealer.hand.values()) > 21:
            self.round_ace_transform(self.dealer)
            while sum(self.dealer.hand.values()) < 17:
                self.dealer.hit(self.deck)
                self.round_ace_transform(self.dealer)

            if sum(self.dealer.hand.values()) > 21:    
                self.round_print_dealer()   
                self.player.stack += self.player_bet
                print(f"Player win! Delaer busts!")
                print(f"Dealer:{sum(self.dealer.hand.values())} vs Player:{sum(self.player.hand.values())}")
                self.round_hands_reset()

                return False

        self.round_print_dealer()    
        self.round_check()    

    def round_ace_transform(self,p):
        for i in ['A-H','A-C','A-S','A-D']:
            if p.hand.get(i):
                p.hand[i] = 1

    def round_hands_reset(self):
            self.dealer.hand = {}
            self.player.hand = {}

    def round_check(self):
            dealer_sum = sum(self.dealer.hand.values()) 
            player_sum = sum(self.player.hand.values())

            if (dealer_sum > player_sum):
                self.player.stack -= self.player_bet
                self.round_hands_reset()
                print(f"Dealer win!")
                print(f"Dealer:{dealer_sum} vs Player:{player_sum}")
                return True
            elif dealer_sum < player_sum:
                self.player.stack += self.player_bet 
                self.round_hands_reset()
                print(f"Player win!")
                print(f"Dealer:{dealer_sum} vs Player:{player_sum}")
                return True
            elif dealer_sum == player_sum:
                print(f"Equal - nobody win!")
                print(f"Dealer:{dealer_sum} vs Player:{player_sum}")
                self.round_hands_reset()
                return True

    def round_print_dealer(self):
        clear_output()
        print(' '.join(list(self.dealer.hand.keys())))
        print("----------")
        print(' '.join(list(self.player.hand.keys())))

    def round_print_player(self):
        clear_output()
        print(f"X {list(self.dealer.hand.keys())[1]}")
        print("----------")
        print(' '.join(list(self.player.hand.keys())))

    def ask_for_continue(self):
        ans = input("Continue? yes/no: ")
        return ans == 'yes'

    def round_play(self):
        print(f"Player stack: {self.player.stack}")
        self.ask_for_bet()
        self.round_print_player()

        if self.player_play() == True:
            self.dealer_play()

        if self.player.stack > 0:
            return self.ask_for_continue()

        else:
            print("Stack devastated!")   