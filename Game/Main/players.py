import pygame, game


class Player:
    def __init__(self, name, icolor,acolor, ships, cards):
        self.Name = name
        self.aColor = acolor
        self.iColor = icolor
        self.Ships = []
        self.Cards = []
        self.Turn = False
        self.shipsplaced = 0


    
#def switchTurn(player,players):
#	MaxIndex- len(players)-1
#	j=0
#	for f in range(MaxIndex):
#		j-1
#		if(player == players[i]):
#			if (i==MaxIndex):
#				j=0
#			else:
#				j+=1
#	return players[j]

################ TEST ####################
#a=player('a')
#b= plater('b')

#players = [a,b]
#ActivePlayer = a

#print(ActivePlayer.naam)

#for i in range(10):
	#activePlayer = switchTrun(ActivePlayer, Players)
	#print(ActivePlayer.naam)