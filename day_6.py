def get_guard_position(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                return (i, j)

def predict_path(map):
    movement = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

    next_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}

    positions = 1
    direction = "^"

    r, c = get_guard_position(map)
    map[r][c] != "X"

    rows = len(map)
    cols = len(map[0])

    while 0 <= r < rows and 0 <= c < cols:
        
        r += movement[direction][0]
        c += movement[direction][1]
        
        if 0 <= r < rows and 0 <= c < cols:
            if map[r][c] != "#":
                if map[r][c] != "X":
                    positions += 1
                    map[r][c] = "X"
            else:
                r -= movement[direction][0]
                c -= movement[direction][1]
                direction = next_direction[direction]
    return positions


def get_obstructions(map):
    r, c = get_guard_position(map)
    start = (r, c)
    count = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i, j) != start and map[i][j] == ".":
                map[i][j] = "#"
                if check_loop(map, start):
                    count += 1
                map[i][j] = "."
    return count


def check_loop(map, start):
    movement = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

    next_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}

    direction = "^"
    r, c = start
    rows = len(map)
    cols = len(map[0])
    save_directions = {}

    while 0 <= r < rows and 0 <= c < cols:
        r += movement[direction][0]
        c += movement[direction][1]
        
        if 0 <= r < rows and 0 <= c < cols:

            if map[r][c] != "#":
                pos = (r, c)
                if save_directions.get(pos, "!") == direction:
                    return True
                save_directions[pos] = direction

            else:
                r -= movement[direction][0]
                c -= movement[direction][1]
                direction = next_direction[direction]
    return False

map = []
while True:
    line = input()
    if line == "":
        break
    map.append(list(line))

print(get_obstructions(map))