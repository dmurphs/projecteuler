#sort hand
def organize_hand(hand, value_dict):
    for i in range(5):
        num = value_dict[hand[i][0]]
        card = (num, hand[i][1])
        hand[i] = card
        hand.sort(key=lambda tup: tup[0])

#check for a straight
def is_consecutive(hand):
    for i in range(4):
        if hand[i+1][0] != hand[i][0] + 1:
            return False
    return hand[0][0]

#check too see if all cards are of same suit
def same_suits(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True

#check for the highest number of the same value card
def high_num_of_pairs(hand):
    high_num_of_pairs = 1
    for num in range(2, 15):
        num_of_matches = 0
        for card in hand:
            if card[0] == num:
                num_of_matches += 1
        if num_of_matches > high_num_of_pairs:
            high_num_of_pairs = num_of_matches

    match = 0
    if hand[0][0] == hand[1][0]:
        match = hand[0][0]
    elif hand[1][0] == hand[2][0]:
        match = hand[1][0]
    elif hand[2][0] == hand[3][0]:
        match = hand[2][0]
    elif hand[3][0] == hand[4][0]:
        match = hand[3][0]
    
    return high_num_of_pairs, match

#check for full house
def is_full_house(hand):
    if hand[0][0] == hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return hand[0][0], hand[3][0]
    elif hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] == hand[4][0]:
        return hand[0][0], hand[2][0]
    else:
        return False

#check for two pair
def is_two_pair(hand):
    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
        return hand[0][0], hand[2][0]
    elif hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
        return hand[0][0], hand[3][0]
    elif hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return hand[1][0], hand[3][0]
    else:
        return False
    
                
#determine value of hand
def determine_hand(sorted_hand):
    if is_consecutive(sorted_hand) and sorted_hand[0][0] >= 10 and same_suits(sorted_hand):
        return ['royal', "Wowww!"]

    elif is_consecutive(sorted_hand) != False and same_suits(sorted_hand):
        return ['straight_flush', is_consecutive(sorted_hand)]

    elif high_num_of_pairs(sorted_hand)[0] == 4:
        return ['four', high_num_of_pairs(sorted_hand)[1]]

    elif is_full_house(sorted_hand) != False:
        return ['full_house', (is_full_house(sorted_hand)[0] + is_full_house(sorted_hand)[1])/2]

    elif is_consecutive(sorted_hand) != False:
        return ['straight', is_consecutive(sorted_hand)]

    elif high_num_of_pairs(sorted_hand)[0] == 3:
        return ['three', high_num_of_pairs(sorted_hand)[1]]

    elif is_two_pair(sorted_hand) != False:
        return ['two_pairs', (is_two_pair(sorted_hand)[0] + is_two_pair(sorted_hand)[1])/2]

    elif high_num_of_pairs(sorted_hand)[0] == 2:
        return ['one_pair', high_num_of_pairs(sorted_hand)[1]]

    else:
        return ['high', sorted_hand[4][0]]

#set scores for each hand and a value reference for cards
poker_scores = {'high': 1, 'one_pair': 2, 'two_pairs': 3, 'three': 4, 'straight': 5, 'flush': 6, 'full_house': 7, 'four': 8, 'straight_flush': 9, 'royal': 10}
value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

#parse lines into hands
with open('poker.txt', 'r') as poker_hands:
    player1_wins = 0
    for line in poker_hands:
        cards = line.split()
        player1_hand = cards[:5]
        player2_hand = cards[5:]

        organize_hand(player1_hand, value_dict)
        organize_hand(player2_hand, value_dict)
        player1_weight = determine_hand(player1_hand)[0]
        player2_weight = determine_hand(player2_hand)[0]

        player1_score = poker_scores[player1_weight]
        player2_score = poker_scores[player2_weight]

        if player1_score == player2_score:
            player1_score += determine_hand(player1_hand)[1]
            player2_score += determine_hand(player2_hand)[1]

        if player1_score == player2_score:
            player1_score += player1_hand[4][0]
            player2_score += player2_hand[4][0]
            

        if player1_score > player2_score:
            print "Player 1 Wins!"
            player1_wins += 1
        elif player1_score < player2_score:
            print "Player 2 Wins!"
        else:
            print "hmmmmm..."

    print "Player 1 Wins: " + str(player1_wins)

    input("press enter to continue")
