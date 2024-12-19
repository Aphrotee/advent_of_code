import sys, heapq
sys.setrecursionlimit(10**6)

import heapq
from collections import defaultdict

def dijkstra_with_path_count(graph, start, end):
    # Initialize distances and count arrays
    distances = defaultdict(lambda: float('inf'))
    count = defaultdict(int)

    distances[start] = 0
    count[start] = 1

    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if this is not the shortest path to current_node
        if current_distance > distances[current_node]:
            continue

        # Traverse neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                count[neighbor] = count[current_node]  # Reset count to match the new shortest path
                heapq.heappush(pq, (distance, neighbor))

            # Found an equally short path
            elif distance == distances[neighbor]:
                count[neighbor] += count[current_node]

    # Return the count of shortest paths to the end node
    return count[end] if end in count else 0


def traverse(reindeer_map, row, col, rows, cols):
    

    pq = [(0, (row, col), (0, 1))]
    distances = {}
    target = None
    count = {}
    for i in range(rows):
        for j in range(cols):
            distances[(i, j)] = float('inf')
            count[(i, j)] = 0
            if reindeer_map[i][j] == 'E':
                target = (i, j)
    count[(row, col)] = 1
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq:
        score, (r, c), dir = heapq.heappop(pq)

        if score > distances[(r, c)]:
            continue

        for dr, dc in dirs:

            d_score = 1
            nr, nc = r + dr, c + dc

            if (dr, dc) != dir:
                d_score += 1000
            
            new_score = score + d_score

            if 0 <= nr < rows and 0 <= nc < cols:

                if reindeer_map[nr][nc] != "#":
                    print(count[(nr, nc)],count[(r, c)])
                    if new_score < distances[(nr, nc)]:
                        distances[(nr, nc)] = new_score
                        count[(nr, nc)] = count[(r, c)]
                        heapq.heappush(pq, (new_score, (nr, nc), (dr, dc)))
                    
                    elif new_score == distances[(nr, nc)]:
                        count[(nr, nc)] += count[(r, c)]

    print(count[target])

    return distances[target]


def get_score(reindeer_map):
    rows = len(reindeer_map)
    cols = len(reindeer_map[0])

    for i in range(rows):
        for j in range(cols):
            if reindeer_map[i][j] == 'S':
                return traverse(reindeer_map, i, j, rows, cols)

def main():
    reindeer_map = []
    while True:
        line = input()
        if line == "":
            break
        reindeer_map.append(line)
    print(get_score(reindeer_map))

main()