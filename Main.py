from random import shuffle
from random import choice
from ImageCopy import images
import tkinter as tk

class Whot(images):
    'A Game of cards usually involving two players by default see manual for more info'
    def __init__(self):
        super().__init__()
        
    def InitDepot(self):
        Whot.Cards = self._DepotMarket.copy()
        shuffle(Whot.Cards)
        #return Whot.Cards

    def NormCards(self):
        'Normalize the cards if startcard has whot 20 in it'
        if self.PlayedCards()[len(self.PlayedCards())-1][1][1] == 20:
            try:
                misc_cards = []
                for i in range(4):
                    misc_cards.append(Whot.Cards[i])
                    Whot.Cards.pop(i)
                shuffle(misc_cards)
                self.PlayedCards().append(choice(misc_cards))
                self.NormCards()
            except:
                #self.NormCards()
                pass
            
        
    def InitPlayerCards(self):
        'Initialize player cards and Starting (played) cards'
        self._startcard1 = []
        self._startcard2 = []
        for i in range(5):
            self._startcard1.append(Whot.Cards[i])
            Whot.Cards.pop(i)
        for i in range(5):
            self._startcard2.append(Whot.Cards[i])
            Whot.Cards.pop(i)
        _card = choice(Whot.Cards)
        self.PlayedCards().append(_card)
        Whot.Cards.remove(_card)
        #self._completed = []
        pass

    def LoopDepot(self):
        'Loops depot cards if they are less than or equal to 2'
        if len(Whot.Cards) <= 2:
            self.InitDepot()


    def PlayedCards(self, cards=[]):
        'Returns the played cards in a nested tuple'
        return cards

    def InitComputerCards(self):
        'Initializes the cards for Player1 (computer) to start'
        global card1
        card1 = self._startcard1

    def InitPlayer2Cards(self):
        'Initializes the cards for Player2 to start'
        global card2
        card2 = self._startcard2
        
    def ComputerCards(self):
        for i in card1:
            print( i[1])
        #return card1

    def Player2Cards(self):
        for i in card2:
            print( i[1])
        #return card2
    
class Computer(Whot):
    'Objects and attributes for Player1'
    def __init__(self):
        super().__init__()
        self._compup2=[0]
        self._compup8=[0]
        self._compup1=[0]
        self._compup14=[0]
        self._compup20=[0]
        
    def play(self, playcard):
        'Player1 Plays a valid card in his/her cardstack'
        self.LoopDepot()
        if playcard in self.cards():
            if playcard[1][0] == self.PlayedCards()[len(self.PlayedCards())-1][1][0] or\
               playcard[1][1] == self.PlayedCards()[len(self.PlayedCards())-1][1][1] or\
               playcard[1][1] == 20 or self.PlayedCards()[len(self.PlayedCards())-1][1][1] == 20:
                print(playcard[1], "Has been played")
                if playcard[1][1] == 2:
                    self._compup2.insert(0,2)
                    print('Pick Two Cards')
                elif playcard[1][1] == 1:
                    self._compup1.insert(0,1)
                    print('Hold On')
                elif playcard[1][1] == 8:
                    self._compup8.insert(0,8)
                    print("Hold On")
                elif playcard[1][1] == 14:
                    self._compup14.insert(0,14)
                    print("General Market")
                elif playcard[1][1] == 20:
                    self._compup20.insert(0,20)
                    print('Ask for a card...')
                self.PlayedCards().append(playcard)
                self.cards().remove(playcard)
                if len(self.cards()) == 1:
                    print("Last Card")
                elif len(self.cards()) == 0:
                    print("Checkmate.....!")
                    #exit()
                return True
            else:
                raise WhotException("Error: Invalid Move!")
                #return False
        else:
            raise WhotException("Error: Playcard is not in your cardstack!")
            #return False

    def cards(self):
        "returns player1's (computer) cards"
        return card1

    def gomart(self):
        'Sends Player1 to Market'
        self.LoopDepot()
        _card = choice(Whot.Cards)
        self.cards().append(_card)
        Whot.Cards.remove(_card)


class Player2(Whot):
    'Objects and attributes for Player2'
    def __init__(self):
        super().__init__()
        self._player2up2=[0]
        self._player2up1=[0]
        self._player2up8=[0]
        self._player2up14=[0]
        self._player2up20=[0]
        
    def play(self, playcard):
        'Player2 Plays a valid card in his/her cardstack'
        self.LoopDepot()
        if playcard in self.cards():
            if playcard[1][0] == self.PlayedCards()[len(self.PlayedCards())-1][1][0] or\
               playcard[1][1] == self.PlayedCards()[len(self.PlayedCards())-1][1][1] or\
               playcard[1][1] == 20 or self.PlayedCards()[len(self.PlayedCards())-1][1][1] == 20:
                print(playcard[1], "Has been played")
                if playcard[1][1] == 2:
                    self._player2up2.insert(0,2)
                    print('Pick Two Cards')
                elif playcard[1][1] == 1:
                    self._player2up1.insert(0,1)
                    print('Hold On')
                elif playcard[1][1] == 8:
                    self._player2up8.insert(0,8)
                    print("Hold On")
                elif playcard[1][1] == 14:
                    self._player2up14.insert(0,14)
                    print("General Market")
                elif playcard[1][1] == 20:
                    self._player2up20.insert(0,20)
                    print('Ask for a card...')
                self.PlayedCards().append(playcard)
                self.cards().remove(playcard)
                if len(self.cards()) == 1:
                    print("Last Card")
                elif len(self.cards()) == 0:
                    print("Checkmate.....!")
                    #exit()
                return True
            else:
                raise WhotException("Error: Invalid Move!")
                #return False
        else:
            raise WhotException("Error: Playcard is not in your cardstack!")
            #return False

    def cards(self):
        "returns Player2's cards"
        return card2

    def gomart(self):
        "Sends player2 to market"
        self.LoopDepot()
        _card = choice(Whot.Cards)
        self.cards().append(_card)
        Whot.Cards.remove(_card)


class WhotException(Exception):
    "Exception for the Whot class"
    def __init__(self, message):
        self.message = message
        self.run()
    def run(self):
        'Return the message'
        return self.message

if __name__ == '__main__':
    yap = tk.Tk()
    app = Whot()
    app.InitDepot()
    app.InitPlayerCards()
    app.InitComputerCards()
    app.InitPlayer2Cards()
    app.NormCards()
    p1 = Computer()
    p2 = Player2()
    pc1 = p1.ComputerCards
    pc2 = p2.Player2Cards
    
