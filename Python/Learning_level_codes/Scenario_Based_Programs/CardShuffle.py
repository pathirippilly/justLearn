master_deck=list(range(1,53))
random.shuffle(master_deck)
master_deck=set(master_deck)
players=5

def deckHandling(master_deck,players_left):
 tot_cards=len(master_deck)
 sample_count=len(master_deck)//players_left
 deck_out=random.sample(master_deck,sample_count)
 return deck_out
while(players>0):
 exec("D{}=deckHandling(master_deck,players)".format(players))
 exec("master_deck=master_deck-set(D{})".format(players))
 players -= 1
