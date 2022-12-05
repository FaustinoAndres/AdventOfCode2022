POINTS = {'rock': 1, 'paper': 2, 'scissors': 3}
POINTS_RESULTS = {'lose': 0, 'draw': 3, 'win': 5}
OPPONENT = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
ME = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
RELATIONS = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}


def puzzle():

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    return lines

def game(round_):

    score = None
    if RELATIONS[ME[round_[1]]] == OPPONENT[round_[0]]:
        score = 6
    elif RELATIONS[OPPONENT[round_[0]]] == ME[round_[1]]:
        score = 0
    else:
        score = 3

    return score

def main():

    rounds = list(map(lambda line: tuple(line.rstrip('\n').split()), puzzle()))

    score = 0
    for round_ in rounds:
        score += POINTS[ME[round_[1]]]
        score += game(round_)


    print(score)

if __name__ == '__main__':

    main()