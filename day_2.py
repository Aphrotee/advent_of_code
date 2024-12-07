count = 0
def check_if_safe(data):
    skips = 0
    inc = True if data[1] > data[0] else False
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            skips += 1
        elif data[i] > data[i - 1] and not inc:
           skips += 1
        elif data[i] < data[i - 1] and inc:
            skips += 1
        elif abs(data[i] - data[i - 1]) > 3:
            skips += 1
    return True if skips == 0 else False
i = 0
while True:
    i += 1
    data = list(map(int, input().split()))
    if len(data) == 0:
        print(count)
        break
    safe = False
    for j in range(len(data) + 1):
        newData = data[:j] + data[j + 1:]
        if check_if_safe(newData) or check_if_safe(newData[::-1]):
            count += 1
            break
exit(0)