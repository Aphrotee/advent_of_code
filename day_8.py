def get_antinodes(first, second):
    x = second[0] - first[0]
    y = second[1] - first[1]

    a1 = (first[0] - x, first[1] - y)
    a2 = (second[0] + x, second[1] + y)
    return (a1, a2)

def get_all_antinodes(first, second, rows, cols):
    x = second[0] - first[0]
    y = second[1] - first[1]

    a1 = first
    a2 = second
    mul = 0
    antinodes = set()
    while (0 <= a1[0] < rows and 0 <= a1[1] < cols) or (0 <= a2[0] < rows and 0 <= a2[1] < cols):
        if 0 <= a1[0] < rows and 0 <= a1[1] < cols:
            antinodes.add(a1)
        if 0 <= a2[0] < rows and 0 <= a2[1] < cols:
            antinodes.add(a2)
        a1 = (first[0] - (x * mul), first[1] - (y * mul))
        a2 = (second[0] + (x * mul), second[1] + (y * mul))
        mul += 1
    return antinodes

def get_antinodes_count(map):
    rows = len(map)
    cols = len(map[0])
    store = {}
    count = set()
    for i in range(rows):
        for j in range(cols):
            if map[i][j] not in "#." :
                arr = store.get(map[i][j], [])
                arr.append((i, j))
                store[map[i][j]] = arr
    for antenna in store:
        positions = store[antenna]
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                first, second = get_antinodes(positions[i], positions[j])
                if 0 <= first[0] < rows and 0 <= first[1] < cols:
                        count.add(first)
                if 0 <= second[0] < rows and 0 <= second[1] < cols:
                        count.add(second)
    return len(count)

def get_antinodes_count_2(map):
    rows = len(map)
    cols = len(map[0])
    store = {}
    count = set()
    for i in range(rows):
        for j in range(cols):
            if map[i][j] not in "#." :
                arr = store.get(map[i][j], [])
                arr.append((i, j))
                store[map[i][j]] = arr
    for antenna in store:
        positions = store[antenna]
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                antinodes = get_all_antinodes(positions[i], positions[j], rows, cols)
                for a in antinodes:
                    count.add(a)                
    return len(count)

def main():
    map = []
    while True:
        line = input()
        if line == "":
            break
        map.append(line)
    print(get_antinodes_count_2(map))

main()