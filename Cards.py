#!/usr/bin/env python
# coding: utf-8

# In[1]:


# CARD GAME - "WAR"
# SUIT,RANK,VALUE
import random
#random is used to do some random shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# In[3]:


three_of_clubs=Card("Clubs",'Three')


# In[4]:


three_of_clubs.suit


# In[5]:


three_of_clubs.value


# In[ ]:





# In[6]:


two_hearts = Card("Hearts","Two")


# In[7]:


two_hearts


# In[8]:


print(two_hearts)


# In[9]:


two_hearts.suit


# In[10]:


two_hearts.rank


# In[11]:


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}


# In[12]:


values[two_hearts.rank]


# In[13]:


two_hearts.value == three_of_clubs.value


# In[46]:


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)  
        
    def deal_one(self):
        return self.all_cards.pop()


# In[47]:


new_deck = Deck()


# In[48]:


new_deck.shuffle()


# In[49]:


mycard = new_deck.deal_one()


# In[50]:


print(mycard)


# In[51]:


len(new_deck.all_cards)


# In[ ]:





# In[ ]:





# In[52]:


bottom_card = new_deck.all_cards[-1]


# In[53]:


print(bottom_card)


# In[54]:


new_deck.shuffle()


# In[55]:


print(new_deck.all_cards[0])


# In[56]:


class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)
     
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'


# In[57]:


new_player=Player("Jose")


# In[58]:


print(new_player)


# In[59]:


new_player.add_cards(mycard)


# In[60]:


print(new_player)


# In[62]:


print(new_player.all_cards[0])


# In[63]:


new_player.add_cards([mycard,mycard,mycard])


# In[64]:


print(new_player)


# In[65]:


new_player.remove_one()


# In[66]:


print(new_player)


# In[90]:


# GAME SETUP
player_one= Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[91]:


game_on = True


# In[92]:


round_num = 0

while game_on:
    
    round_num+=1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print('Player One,out of cards! Player Two Wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two,out of cards! Player One Wins!')
        game_on = False
        break
        
    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())



    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False
            
        else:
            print('WAR!')
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("Player TWO unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    
                


# In[ ]:





# In[ ]:





# In[ ]:




