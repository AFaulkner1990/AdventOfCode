ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'


if __name__ == '__main__':
    opponent_code = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
    my_code = {'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
    hand_scores = {ROCK: 1, PAPER: 2, SCISSORS: 3}

    your_score = 0
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            stripped: str = line.strip()
            opponent_hand = opponent_code.get(stripped[0])
            my_hand = my_code.get(stripped[2])
            your_score += hand_scores.get(my_hand)
            if opponent_hand == my_hand:
                your_score += 3
            elif (my_hand == ROCK and opponent_hand == SCISSORS) or \
                    (my_hand == PAPER and opponent_hand == ROCK) or \
                    (my_hand == SCISSORS and opponent_hand == PAPER):
                your_score += 6
    print(your_score)
