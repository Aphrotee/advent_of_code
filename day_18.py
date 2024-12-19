def get_grid(rows, cols):
    return [["." for _ in range(cols)] for _ in range(rows)]

def get_shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, 0, 0)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    visited.add((0, 0))
    while pq:
        steps, x, y = pq.pop(0)
        if grid[y][x] == "#":
            continue
        if x == cols - 1 and y == rows - 1:
            return steps
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited:
                visited.add((nx, ny))
                pq.append((steps + 1, nx, ny))
    return -1


def main():
    grid = get_grid(71, 71)
    remaining_bytes = []
    count = 0
    while True:
        line = input()
        if line == "":
            break
        x, y = list(map(int, line.split(",")))
        if count < 1024:
            grid[y][x] = "#"
        else:
            remaining_bytes.append((x, y))
        count += 1
    
    while remaining_bytes:
        x, y = remaining_bytes.pop(0)
        grid[y][x] = "#"
        if get_shortest_path(grid) == -1:
            print("Cut off", x, y)
            break
main()