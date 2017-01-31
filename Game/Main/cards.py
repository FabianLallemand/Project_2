import pygame

class Cards:
    def __init__(self, name,action):
        self.Name = name
        self.Action = action

#offensieve kaarten
card1 = Cards("FMJ Upgrade",None)
card2 = Cards("Rifling",None)
card3 = Cards("Adv Rifling",None)
card4 = Cards("Naval Mine",None)
card5 = Cards("EMP Upgrade",None)
#defensieve kaarten
card6 = Cards("Hull",None)
card7 = Cards("Sonar",None)
card8 = Cards("Smokescreen",None)
card9 = Cards("Sabotage",None)
#Helpende kaarten
card10 = Cards("Backup",None)
card11 = Cards("Extrafuel2",None)
card12 = Cards("Extrafuel",None)
card13 = Cards("Rally",None)
card14 = Cards("Adr. Rush",None)
#speciale kaarten
card15 = Cards("Repair",None)
card16 = Cards("Flak Armor",None)
card17 = Cards("Hack Intel",None)
card18 = Cards("Far Sight",None)
card19 = Cards("Allu. Hull",None)
card20 = Cards("J. Sparrow",None)