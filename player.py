import random
import sys
import time


class PlayerNode:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.playerPosition = 0


winnerList = list()


class PlayerList:
    def __init__(self):
        self.head = None
        self.playersNo = 0
        self.currentPlayer = None
        self.winnerList = list()
        self.noOfDices = 1

    def noOfPlayers(self, nos=4):
        self.playersNo = nos

    def addPlayer(self, data, count):
        newNode = PlayerNode(data)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        if count == self.playersNo:
            newNode.next = self.head

    def gameTurn(self):
        if self.currentPlayer == None:
            self.currentPlayer = self.head
        newPlayer = self.currentPlayer
        nep = random.randint(1, self.noOfDices*6)
        if nep == self.noOfDices*6:
            while nep % (self.noOfDices*6) == 0:
                nep1 = random.randint(1, self.noOfDices*6)
                print(f'Got {self.noOfDices*6} play again')
                input('Press Enter to roll a dice')
                nep += nep1
                if nep == self.noOfDices*18:
                    print('You got 3 times 6 All got cancelled')
                    nep = 0
                    break
        npcp = newPlayer.playerPosition
        if npcp+nep < 101:
            newPlayer.playerPosition += nep
        if newPlayer.playerPosition != 100:
            print(
                f'{self.currentPlayer.data} rolled a {nep} and moved from {npcp} to {newPlayer.playerPosition}', end="")
        else:
            print(f'{self.currentPlayer.data} won the game')
            if self.currentPlayer.data not in self.winnerList:
                self.winnerList.append(self.currentPlayer.data)
            if self.playersNo == len(self.winnerList)+1:
                print("Score Board:")
                print(f'Winner No\t\tPlayer')
                for x in range(len(self.winnerList)):
                    print(x+1, "\t\t\t", self.winnerList[x])
                time.sleep(35)
                sys.exit()
        tenp = self.currentPlayer
        while tenp.next.data in self.winnerList:
            tenp = tenp.next
        self.currentPlayer = tenp.next

        return newPlayer, newPlayer.playerPosition
    # def removePlayer(self,winner):


def checkSnakeOrLadder(slplayer, slplayerpos, cell1, cell2):
    if cell1 != None:
        slplayer.playerPosition = cell2
        if cell1 == "S":
            print(
                f'\nOOPS! Snake Attack,{slplayer.data} moved from {slplayerpos} to {cell2}', end="")
        else:
            print(
                f'\nCongrats! Hit The Ladder,{slplayer.data} moved from {slplayerpos} to {cell2}', end="")
