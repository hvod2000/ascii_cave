from cave import Cave, LevelsTopology, wall
from random import randint, choice
from lib.getchlib import getch

keys = {"up": "cw", "down": "ts", "left": "ra", "right": "nd"}


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


def read_graph_from_binary(source):
    cave = source.replace(" ", "").replace("\t", "").strip().split("\n")
    n = int(cave[0])
    lvl_graph = {i: set() for i in range(n)}
    for u in range(n):
        for v, c in enumerate(map(int, cave[u + 1])):
            if c:
                lvl_graph[u].add(v)
    lvls = LevelsTopology.from_available_moves(lvl_graph)
    return Cave.from_levels_topology(lvls)


def read_graph_from_edges(source):
    cave = source.strip().split("\n")
    n = int(cave[0])
    lvl_graph = {}
    for line in map(lambda s: s.strip(), cave[1:]):
        u, vs = line.split(":")
        u = int(u)
        lvl_graph[u] = set()
        for v in (int(v) for v in vs.strip().split(" ") if v):
            lvl_graph[u].add(v)
    lvls = LevelsTopology.from_available_moves(lvl_graph)
    return Cave.from_levels_topology(lvls)


def add_noise_to_image(layer):
    for y in range(len(layer)):
        for x in range(len(layer[0])):
            if randint(1, 4) == 1:
                layer[y][x] = choice("[]^!><&/-{}?(:#$|~+\%=")


from pathlib import Path
from sys import argv

map_path = "default.map" if len(argv) < 2 else argv[1]
cave = read_graph_from_edges(Path(map_path).read_text())

player = random_player_position(cave)
done = False
while not done:
    print("\n" * 100)
    layer = layer2str(cave, player[2])
    add_noise_to_image(layer)
    layer[~player[1]][player[0]] = "@"
    print("  GET TO FINISH ROOM #1!")
    print("\t" + "\n\t".join("".join(row) for row in layer))
    if isinstance(cave[player], int) and cave.items[cave[player]] == 1:
        print()
        print("CONGRATUATIONS ON YOUR HAED!")
        print("YOU WON!")
        while getch() != "q":
            continue
        break
    c = getch()
    done = c == "q"
    target = list(player)
    if c in keys["up"]:
        target[1] += 1
    elif c in keys["right"]:
        target[0] += 1
    elif c in keys["down"]:
        target[1] -= 1
    elif c in keys["left"]:
        target[0] -= 1
    while cave[target] is not wall:
        player = list(target)
        target[2] -= 1
