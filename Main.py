#from ClassWhotGtk import WhotGtk as WG
from random import shuffle
from random import choice
from ImageCopy import images
import tkinter as tk

class Whot(images):
    #def __init__(self):
    #    images.__init__(Whot)

    def InitDepot(self):
        images.__init__(Whot)
        Whot.Cards = self._DepotMarket.copy()
        shuffle(Whot.Cards)
        #return Whot.Cards
        
    def InitPlayerCards(self):
        self._startcard1 = []
        self._startcard2 = []
        for i in Whot.Cards[0], Whot.Cards[1], Whot.Cards[2], Whot.Cards[3], Whot.Cards[4]:
            self._startcard1.append(i)
        for i in Whot.Cards[5], Whot.Cards[6], Whot.Cards[7], Whot.Cards[8], Whot.Cards[9]:
            self._startcard2.append(i)
        self.PlayedCards().append(Whot.Cards[10])
        pass

    def PlayedCards(self, cards=[]):
        return cards

    def InitComputerCards(self):
        global card1
        card1 = self._startcard1

    def InitPlayer2Cards(self):
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
    def play(self, playcard):
        if playcard in self.cards():
            if playcard[1][0] == self.PlayedCards()[len(self.PlayedCards())-1][1][0] or\
               playcard[1][1] == self.PlayedCards()[len(self.PlayedCards())-1][1][1] or\
               playcard[1][1] == 20:
                print(playcard[1], "Has been played")
                if playcard[1][1] == 2:
                    print('Pick Two Cards')
                elif playcard[1][1] == 1:
                    print('Hold On')
                elif playcard[1][1] == 8:
                    print("Hold On")
                elif playcard[1][1] == 14:
                    print("General Market")
                elif playcard[1][1] == 20:
                    print('Ask for a card...')
                self.PlayedCards().append(playcard)
                self.cards().remove(playcard)
                if len(self.cards()) == 1:
                    print("Last Card")
                elif len(self.cards()) == 0:
                    print("Checkmate.....!")
                    exit()
                return True
            else:
                raise WhotException("Error: Invalid Move!")
                return False
        else:
            raise WhotException("Error: Playcard is not in youur cardstack!")
            return False

    def cards(self):
        return card1

    def gomart(self):
        self.cards().append(Whot.Cards[11])
        Whot.Cards.remove(Whot.Cards[11])

    def gogenmart(self):
        self.cards().append(Whot.Cards[12])
        Whot.Cards.remove(Whot.Cards[12])

class Player2(Whot):
    def play(self, playcard):
        if playcard in self.cards():
            if playcard[1][0] == self.PlayedCards()[len(self.PlayedCards())-1][1][0] or\
               playcard[1][1] == self.PlayedCards()[len(self.PlayedCards())-1][1][1] or\
               playcard[1][1] == 20:
                print(playcard[1], "Has been played")
                if playcard[1][1] == 2:
                    print('Pick Two Cards')
                elif playcard[1][1] == 1:
                    print('Hold On')
                elif playcard[1][1] == 8:
                    print("Hold On")
                elif playcard[1][1] == 14:
                    print("General Market")
                elif playcard[1][1] == 20:
                    print('Ask for a card...')
                self.PlayedCards().append(playcard)
                self.cards().remove(playcard)
                if len(self.cards()) == 1:
                    print("Last Card")
                elif len(self.cards()) == 0:
                    print("Checkmate.....!")
                    exit()
                return True
            else:
                raise WhotException("Error: Invalid Move!")
                return False
        else:
            raise WhotException("Error: Playcard is not in your cardstack!")
            return False

    def cards(self):
        return card2

    def gomart(self):
        self.cards().append(Whot.Cards[13])
        Whot.Cards.remove(Whot.Cards[13])

    def gogenmart(self):
        self.cards().append(Whot.Cards[14])
        Whot.Cards.remove(Whot.Cards[14])

class WhotException(Exception):
    def __init__(self, message):
        self.message = message
        self.run()
    def run(self):
        return self.message

if __name__ == '__main__':
    yap = tk.Tk()
    app = Whot()
    app.InitDepot()
    app.InitPlayerCards()
    app.InitComputerCards()
    app.InitPlayer2Cards()
    p1 = Computer()
    p2 = Player2()
    pc1 = p1.ComputerCards
    pc2 = p2.Player2Cards
    
    #WG(yap)
