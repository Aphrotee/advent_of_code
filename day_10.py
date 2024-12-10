def get_score(r, c, map, rows, cols):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    end = set()
    queue = [(r, c, 0)]
    while queue:
        row, col, current = queue.pop(0)

        if current == 9:
            end.add((row, col))
            continue
        
        for dr, dc in dirs:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and map[nr][nc] == current + 1:
                queue.append((nr, nc, current + 1))
    return len(end)


def get_total_score(map):
    rows = len(map)
    cols = len(map[0])
    answer = 0

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 0:
                answer += get_score(i, j, map, rows, cols)
    return answer

def get_rating(r, c, map, rows, cols):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    trails = list()
    queue = [(r, c, 0, [(r, c)])]
    while queue:
        row, col, current, path = queue.pop(0)

        if current == 9:
            trails.append(path)
            continue
        
        for dr, dc in dirs:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and map[nr][nc] == current + 1:
                queue.append((nr, nc, current + 1, path + [(nr, nc)]))
    return len(trails)


def get_total_rating(map):
    rows = len(map)
    cols = len(map[0])
    answer = 0

    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 0:
                answer += get_rating(i, j, map, rows, cols)
    return answer

def main():
    skymap = []
    while True:
        line = input()
        if line == '':
            break
        skymap.append(list(map(int, line)))

    print(get_total_rating(skymap))


main()