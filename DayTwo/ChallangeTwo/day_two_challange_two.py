ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
WIN = 'Win'
DRAW = 'Draw'
LOSE = 'Lose'


if __name__ == '__main__':
    opponent_code = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
    my_code = {'X': LOSE, 'Y': DRAW, 'Z': WIN}
    hand_scores = {ROCK: 1, PAPER: 2, SCISSORS: 3}

    def get_hand(o_hand, should_do):
        if should_do == LOSE:
            if o_hand == ROCK:
                return SCISSORS
            elif o_hand == PAPER:
                return ROCK
            else:
                return PAPER
        elif should_do == DRAW:
            if o_hand == ROCK:
                return ROCK
            elif o_hand == PAPER:
                return PAPER
            else:
                return SCISSORS
        else:
            if o_hand == ROCK:
                return PAPER
            elif o_hand == PAPER:
                return SCISSORS
            else:
                return ROCK


    your_score = 0
    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            stripped: str = line.strip()
            opponent_hand = opponent_code.get(stripped[0])
            what_should_do = my_code.get(stripped[2])
            my_hand = get_hand(opponent_hand, what_should_do)
            your_score += hand_scores.get(my_hand)
            if opponent_hand == my_hand:
                your_score += 3
            elif (my_hand == ROCK and opponent_hand == SCISSORS) or \
                    (my_hand == PAPER and opponent_hand == ROCK) or \
                    (my_hand == SCISSORS and opponent_hand == PAPER):
                your_score += 6
    print(your_score)
