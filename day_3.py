# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)

ans = [0]

def parse(line, enable):
    index = [0]
    length = len(line)
    enable_mul = enable

    def mul(length):
        x_str = []
        y_str = []
        
        if line[index[0]:index[0] + 3] == "mul":
            index[0] += 3
            if index[0] < length and line[index[0]] == "(":
                index[0] += 1    
                while index[0] < length and line[index[0]].isdigit():
                    x_str.append(line[index[0]])
                    index[0] += 1
                if index[0] < length and line[index[0]] == ",":
                    index[0] += 1
                    while index[0] < length and line[index[0]].isdigit():
                        y_str.append(line[index[0]])
                        index[0] += 1
                    if index[0] < length and line[index[0]] == ")":
                        if x_str and y_str:
                            print("".join(x_str), "".join(y_str))
                            return int("".join(x_str)) * int("".join(y_str))
        return 0
    while index[0] < length:
        if line[index[0]] == "m" and enable_mul:
            ans[0] += mul(length)
        elif line[index[0]: index[0] + 4] == "do()":
            enable_mul = True
            index[0] += 3
        elif line[index[0]: index[0] + 7] == "don't()":
            enable_mul = False
            index[0] += 6
        index[0] += 1
    return enable_mul
enable = True
while True:
    line = input()
    if line == "":
        break
    enable = parse(line, enable)
    print(ans[0])
exit(0)