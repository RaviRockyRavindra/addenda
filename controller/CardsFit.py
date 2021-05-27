## class to set rnks and suits

import random

class Card(object):
    def __init__(self,rank,suite):
        self.rank = rank
        self.suite = suite
        self.__repr__()

    # def display(self):
    #     print('%s of %s' % (self.rank,self.suite))
 
    def __repr__(self):
        return f'{self.rank} of {self.suite}'


class Deck(object):
    values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    def __init__(self):
        self.cards=[]
        self.make()
        
    #     
    def make(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for c in self.values:
                self.cards.append(Card(c,s))

    def display(self):
        for c in self.cards:
            c.display()

    # fisher yate algo for card shuffiling

    def shuffle_cards(self):
        local_array=self.cards
        for i in range(len(local_array)-1,0,-1):
            j = random.randint(0,i+1)
            local_array[i],local_array[j] = local_array[j],local_array[i]
        return list(local_array)


# # Deck().display()    
# shuffle_cards = Deck().shuffle_cards()
# print(shuffle_cards)
# for s in shuffle_cards:
#     print(s)