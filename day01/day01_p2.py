
def puzzle():

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    return lines

def main():

    lines = list(map(lambda line: line.rstrip('\n'), puzzle()))
    elves = {}
    elf = 0
    calories = 0
    for line in lines:
        if line != '':
            calories += int(line)
        else:
            elf += 1
            elves[elf] = calories
            calories = 0

    print(sum(sorted(list(elves.values()))[-3:]))

if __name__ == '__main__':

    main()