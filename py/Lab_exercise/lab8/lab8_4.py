import random
deck=list(range(52))
random.shuffle(deck)

suit_list=['spades','hearts','diamonds','clubs']
card_rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
for i in range(4):
    suit=suit_list[deck[i]//13]
    rank=card_rank[deck[i]%13]
    print(f"Card {i+1}: {suit} , {rank}")
