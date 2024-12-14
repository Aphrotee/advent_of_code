# --- Day 13: Claw Contraption ---
# Next up: the lobby of a resort on a tropical island. The Historians take a moment to admire the hexagonal floor tiles before spreading out.

# Fortunately, it looks like the resort has a new arcade! Maybe you can win some prizes from the claw machines?

# The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons
# labeled A and B. Worse, you can't just put in a token and play; it costs 3 tokens to push the A button and 1 token to push the B button.

# With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the
# right (along the X axis) and a specific amount forward (along the Y axis) each time that button is pressed.

# Each machine contains one prize; to win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.

# You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every
# machine's button behavior and prize location (your puzzle input). For example:

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# This list describes the button configuration and prize location of four different claw machines.

# For now, consider just the first claw machine in the list:

# Pushing the machine's A button would move the claw 94 units along the X axis and 34 units along the Y axis.
# Pushing the B button would move the claw 22 units along the X axis and 67 units along the Y axis.
# The prize is located at X=8400, Y=5400; this means that from the claw's initial position, it would need to move exactly 8400 units along
# the X axis and exactly 5400 units along the Y axis to be perfectly aligned with the prize in this machine.
# The cheapest way to win the prize is by pushing the A button 80 times and the B button 40 times. This would line up the claw along the
# X axis (because 80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this would cost 80*3 tokens for the A presses
# and 40*1 for the B presses, a total of 280 tokens.

# For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.

# For the third claw machine, the cheapest way to win the prize is by pushing the A button 38 times and the B button 86 times. Doing this would cost a total of 200 tokens.

# So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is 480.

# You estimate that each button would need to be pressed no more than 100 times to win a prize. How else would someone be expected to play?

# Figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?

# Your puzzle answer was 31552.

# --- Part Two ---
# As you go to win the first prize, you discover that the claw is nowhere near where you expected it would be. Due to a unit conversion error
# in your measurements, the position of every prize is actually 10000000000000 higher on both the X and Y axis!

# Add 10000000000000 to the X and Y position of every prize. After making this change, the example above would now look like this:

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=10000000008400, Y=10000000005400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=10000000012748, Y=10000000012176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=10000000007870, Y=10000000006450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=10000000018641, Y=10000000010279
# Now, it is only possible to win a prize on the second and fourth claw machines. Unfortunately, it will take many more than 100 presses to do so.

# Using the corrected prize coordinates, figure out how to win as many prizes as possible. What is the fewest tokens you would have to spend to win all possible prizes?

# Your puzzle answer was 95273925552482.

# Both parts of this puzzle are complete! They provide two gold stars: **

def parse_query(query):
    a = query[0].split()
    ax = a[2]
    ay = a[3]
    b = query[1].split()
    bx = b[2]
    by = b[3]
    target = query[2].split()
    tx = target[1]
    ty = target[2]
    # output = {"A": {"x": int(ax[2:-1]), "y": int(ay[2:])}, "B": {"x": int(bx[2:-1]), "y": int(by[2:])}, "prize": {"x": int(tx[2:-1]), "y": int(ty[2:])}}
    output = {"A": {"x": int(ax[2:-1]), "y": int(ay[2:])}, "B": {"x": int(bx[2:-1]), "y": int(by[2:])}, "prize": {"x": 10000000000000 + int(tx[2:-1]), "y": 10000000000000 + int(ty[2:])}}
    return output

def get_min_cost(query):
    prize = (query["prize"]["x"], query["prize"]["y"])

    start = ((0, 0), 100, 0)

    queue = [start]

    answer = float("inf")
    visited = set()

    while queue:
        current, a, b = queue.pop(0)

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # print(answer, current, a, b)


        if current[0] > prize[0] or current[1] > prize[1]:
            continue
        if current == prize:
            answer = min(answer, (a * 3) + b)
            break
            
        if (a + 1, b) not in visited:
            queue.append(((current[0] + query["A"]["x"], current[1] + query["A"]["y"]), a + 1, b))

        if (a, b + 1) not in visited:
            queue.append(((current[0] + query["B"]["x"], current[1] + query["B"]["y"]), a, b + 1))

    return answer if answer < float("inf") else 0

def get_min_cost3(a1, a2, a3, a4, c1, c2):

    det = (a1 * a4) - (a2 * a3)

    det1 = (c1 * a4) - (c2 * a2)

    det2 = (a1 * c2) - (a3 * c1)

    if det1 % det == 0 and det2 % det == 0:
        return (det1 // det, det2 // det)
    return (0, 0)

def main():
    queries = []

    empty = 0
    query = []
    while True:
        line = input()
        if line == "":
            if query:
                queries.append(parse_query(query[:]))
            query = []
            empty += 1
            if empty >= 2:
                break
        else:
            empty = 0
            query.append(line)
    
    mincost = 0
    for q in queries:
        # mincost += get_min_cost2(q)
        # a, b = solve_simultaneous_equations([[q["A"]["x"], q["B"]["x"]], [q["A"]["y"], q["B"]["y"]]], [q["prize"]["x"], q["prize"]["y"]])
        a, b = get_min_cost3(q["A"]["x"], q["B"]["x"], q["A"]["y"], q["B"]["y"], q["prize"]["x"], q["prize"]["y"]) 
        print(a, b)
        # if check_int(a) and check_int(b):
        mincost += ((int(a) * 3) + int(b))
    print(mincost)

main()