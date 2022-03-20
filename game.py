from cave import Cave, LevelsTopology, wall
from random import randint, choice
from lib.getchlib import getch


def layer2str(cave, z, f=str):
    layer, floor, items = cave.cells[z], cave.cells[z - 1], cave.items
    result = []
    for y in range(len(layer) - 1, -1, -1):
        result.append([])
        for x, c in enumerate(layer[y]):
            c = f(items[c]) if isinstance(c, int) else " " if c is None else "#"
            c = "." if c == " " and floor[y][x] is not wall else c
            result[-1].append(c)
    return result


def random_player_position(cave):
    while True:
        z = randint(1, len(cave.cells) - 1)
        y = randint(0, len(cave.cells[0]) - 1)
        x = randint(0, len(cave.cells[0][0]) - 1)
        player = [x, y, z]
        under = [x, y, z - 1]
        if cave[player] is not wall and cave[under] is wall:
            return player


cave = ... #TODO

player = random_player_position(cave)
done = False
while not done:
    print("\n" * 100)
    layer = layer2str(cave, player[2], lambda i: str(i + 1))
    layer[~player[1]][player[0]] = "@"
    print("  GET TO FINISH ROOM #1!")
    print("\t" + "\n\t".join("".join(row) for row in layer))
    if isinstance(cave[player], int) and cave.items[cave[player]] == 0:
        print()
        print("CONGRATUATIONS ON YOUR HAED!")
        print("YOU WON!")
        input()
        break
    c = getch()
    done = c == "q"
