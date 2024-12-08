# --- Day 8: Resonant Collinearity ---
# You find yourselves on the roof of a top-secret Easter Bunny installation.

# While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise,
# it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand
# Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

# Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific
# frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas.
# In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same
# frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas
# with the same frequency, there are two antinodes, one on either side of them.

# So, for these two antennas with frequency a, they create the two antinodes marked with #:

# ..........
# ...#......
# ..........
# ....a.....
# ..........
# .....a....
# ..........
# ......#...
# ..........
# ..........
# Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes,
# but two are off the right side of the map, so instead it adds only two:

# ..........
# ...#......
# #.........
# ....a.....
# ........a.
# .....a....
# ..#.......
# ......#...
# ..........
# ..........
# Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However,
# antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A creates
# no antinodes but has a lowercase-a-frequency antinode at its location:

# ..........
# ...#......
# #.........
# ....a.....
# ........a.
# .....a....
# ..#.......
# ......A...
# ..........
# ..........
# The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an
# antinode overlapping the topmost A-frequency antenna:

# ......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.
# Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations
# that contain an antinode within the bounds of the map.

# Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?

# Your puzzle answer was 278.

# --- Part Two ---
# Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

# Whoops!

# After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least
# two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at
# the position of each antenna (unless that antenna is the only one of its frequency).

# So, these three T-frequency antennas now create many antinodes:

# T....#....
# ...T......
# .T....#...
# .........#
# ..#.......
# ..........
# ...#......
# ..........
# ....#.....
# ..........
# In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes!
# This brings the total number of antinodes in the above example to 9.

# The original example now has 34 antinodes, including the antinodes that appear on every antenna:

# ##....#....#
# .#.#....0...
# ..#.#0....#.
# ..##...0....
# ....0....#..
# .#...#A....#
# ...#..#.....
# #....#.#....
# ..#.....A...
# ....#....A..
# .#........#.
# ...#......##
# Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?

# Your puzzle answer was 1067.

# Both parts of this puzzle are complete! They provide two gold stars: **


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