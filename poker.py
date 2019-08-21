from collections import Counter

def is_straight_flush(hands):
    return is_flush(hands) and is_straight(hands) 

def is_flush(hands):
    i = 0
    while i < len(hands) - 1:
        if hands[i][1] != hands[i+1][1]:
            return False
        i += 1
    
    return True

def is_straight(hands):
    sorted_hand = sorted([str2num(hand[0]) for hand in hands])

    j = 0
    while j < len(sorted_hand) -1:
        if sorted_hand[j] != sorted_hand[j+1] - 1:
            return False
        j += 1
    return True

def is_four_card(hands):
    hands_num = [hand[0] for hand in hands]
    c = Counter(hands_num)
    return max(c.values()) == 4

# def has_same_three(hands):
#     hands_num = [hand[0] for hand in hands]
#     c = Counter(hands_num)
#     return max(c.values()) == 3

def is_three_card(hands):
    hands_num = [hand[0] for hand in hands]
    c = Counter(hands_num)
    result = c.values()
    return max(result) == 3 and min(result) == 1

def is_full_house(hands):
    hands_num = [hand[0] for hand in hands]
    c = Counter(hands_num)
    result = c.values()
    return max(result) == 3 and min(result) == 2

def is_one_pair(hands):
    hands_num = [hand[0] for hand in hands]
    c = Counter(hands_num)
    result = c.values()

    return len(result) == 4

def is_two_pair(hands):
    hands_num = [hand[0] for hand in hands]
    c = Counter(hands_num)
    result = c.values()
    return max(result) == 2 and len(result) == 3

def judge_hands(hands):
    if is_one_pair(hands):
        judgement = 1
    elif is_two_pair(hands):
        judgement = 2
    elif is_straight_flush(hands):
        judgement = 8
    elif is_three_card(hands):
        judgement = 3
    elif is_straight(hands):
        judgement = 4
    elif is_flush(hands):
        judgement = 5
    elif is_four_card(hands):
        judgement = 7
    elif is_full_house(hands):
        judgement = 6
    else:
        judgement = 0
    
    return judgement

def str2num(char):
    if char is 'A':
        return 1
    elif char is 'T':
        return 10
    elif char is 'J':
        return 11
    elif char is 'Q':
        return 12
    elif char is 'K':
        return 13
    else:
        return int(char)

def fuck(player1, player2):
    player1_score = judge_hands(player1)
    player2_score = judge_hands(player2)

    if player1_score > player2_score:
        return "PLAYER1 WIN!!"
    elif player1_score == player2_score:
        return "DRAW"
    else:
        return "PLAYER2 WIN!!"

