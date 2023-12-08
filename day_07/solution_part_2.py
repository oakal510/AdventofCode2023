# advent of code day 7, part 1

class Game_hand:
    def __init__(self, game_hand, bid):
        self.game_hand = game_hand
        self.bid = bid
        self.score = 0
        self.sort_order = ''


    def __str__(self):
       return f"{self.game_hand}, {self.bid}"
    

    def get_score(self):
        
        hand_type_strength =    {"five of a kind": 700, "four of a kind": 600, "full house": 500, 
                                "three of a kind": 400, "two pair": 300, "one pair": 200, "high card": 100}

        one_pair_card = ''
        joker_count = self.game_hand.count('J')
        
        for i, card in enumerate(self.game_hand):

            # deal with jokers
            if joker_count > 0:
                # check for five of a kind resulting from jokers
                if joker_count > 3:
                    self.score = hand_type_strength["five of a kind"]
                    break
                # check for four of a kind and higher resulting from jokers
                elif joker_count == 3:
                    short_hand = self.game_hand.replace('J', '')
                    if short_hand[0] == short_hand[1]:
                        self.score = hand_type_strength["five of a kind"]
                        break
                    else:
                        self.score = hand_type_strength["four of a kind"]
                        break
                # check for three of a kind and higher resulting from jokers
                elif joker_count == 2:
                    short_hand = self.game_hand.replace('J', '')
                    if short_hand[0] == short_hand[1] == short_hand[2]:
                        self.score = hand_type_strength["five of a kind"]
                        break
                    elif short_hand[0] == short_hand[1] or short_hand[0] == short_hand[2] or short_hand[1] == short_hand[2]:
                        self.score = hand_type_strength["four of a kind"]
                        break
                    else:
                        self.score = hand_type_strength["three of a kind"]
                        break
                # check for other joker scoring
                elif joker_count == 1:
                    short_hand = self.game_hand.replace('J', '')
                    short_hand = sorted(short_hand)
                    if short_hand[0] == short_hand[1] == short_hand[2] == short_hand[3]:
                        self.score = hand_type_strength["five of a kind"]
                        break
                    elif short_hand[0] == short_hand[1] and short_hand[-2] == short_hand[-1]:
                        self.score = hand_type_strength["full house"]
                        break 
                    elif len(set(short_hand)) == 2:
                        self.score = hand_type_strength["four of a kind"]
                        break
                    elif len(short_hand) == len(set(short_hand)):
                        self.score = hand_type_strength["one pair"]
                        break
                    else:
                        self.score = hand_type_strength["three of a kind"]
                        break
            
            # regular scoring
            # check for high card 
            elif len(self.game_hand) == len(set(self.game_hand)) and joker_count == 0:
                self.score = hand_type_strength["high card"]
                break
            elif i == 0:
                # check for five of a kind
                if self.game_hand.count(card) == 5:
                    self.score = hand_type_strength["five of a kind"] 
                    break
            else:
                # check for four of a kind
                if self.game_hand.count(card) == 4:
                    self.score = hand_type_strength["four of a kind"]
                    break
                # check for three of a kind and full house
                if self.game_hand.count(card) == 3:
                    # check for full house
                    sorted_hand = sorted(self.game_hand)
                    if sorted_hand[0] == sorted_hand[1] and sorted_hand[-2] == sorted_hand[-1]:
                        self.score = hand_type_strength["full house"] 
                        break
                    else:
                        # assign three of a kind
                        self.score = hand_type_strength["three of a kind"] 
                        break
                # check for two pairs
                if self.score == 200 and self.game_hand.count(card) == 2 and one_pair_card != card:
                    self.score = hand_type_strength["two pair"]
                    break
                # check for one pair
                if self.game_hand.count(card) == 2:
                    self.score = hand_type_strength["one pair"]
                    one_pair_card = card
    
    def get_sort_order(self):
        
        order_dict = {"A": "a", "K": 'b', "Q": "c", "T": "d", "9": "e", "8": "f", "7": "g", 
                      "6": "h", "5": "i", "4": "j", "3": "k", "2": "l", "J": "m"}
        
        for card in self.game_hand:
            self.sort_order += order_dict[card]

def calculate_winnings(buffer):

    scores = []

    for line in buffer.splitlines():
        hand, bid = line.split(' ')

        game = Game_hand(hand, bid)
        game.get_score()
        game.get_sort_order()
        
        scores.append(game)

    game_rank_list = sorted((sorted(scores, key=lambda x: x.sort_order, reverse=True)), key=lambda x: x.score,)

    total_winnings = 0

    for rank, game in enumerate(game_rank_list):
        total_winnings += int(game.bid) * (rank + 1)

    return total_winnings


def test_solution():

    with open('test_input.txt', 'r') as file:
        buffer = file.read()

    assert calculate_winnings(buffer) == 5905


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(calculate_winnings(buffer))