import pygame,cardfunctions

class Cards:
    def __init__(self, name,action):
        self.Name = name
        self.Action = action

#offensieve kaarten
card1 = Cards("FMJ Upgrade",cardfunctions.FMJ)
card2 = Cards("Rifling",cardfunctions.FMJ)
card3 = Cards("Adv Rifling",cardfunctions.FMJ)
card4 = Cards("Naval Mine",cardfunctions.FMJ)
card5 = Cards("EMP Upgrade",cardfunctions.FMJ)
#defensieve kaarten
card6 = Cards("Hull",cardfunctions.FMJ)
card7 = Cards("Sonar",cardfunctions.FMJ)
card8 = Cards("Smokescreen",cardfunctions.FMJ)
card9 = Cards("Sabotage",cardfunctions.FMJ)
#Helpende kaarten
card10 = Cards("Backup",cardfunctions.FMJ)
card11 = Cards("Extrafuel2",cardfunctions.FMJ)
card12 = Cards("Extrafuel",cardfunctions.FMJ)
card13 = Cards("Rally",cardfunctions.FMJ)
card14 = Cards("Adr. Rush",cardfunctions.FMJ)
#speciale kaarten
card15 = Cards("Repair",cardfunctions.FMJ)
card16 = Cards("Flak Armor",cardfunctions.FMJ)
card17 = Cards("Hack Intel",cardfunctions.FMJ)
card18 = Cards("Far Sight",cardfunctions.FMJ)
card19 = Cards("Allu. Hull",cardfunctions.FMJ)
card20 = Cards("J. Sparrow",cardfunctions.FMJ)