first = []
second = []
distance = 0

while True:
    try:
        f, s = list(map(int, input().split()))
        first.append(f)
        second.append(s)
    except Exception as e:
        break

# first.sort()
# second.sort()

# for f, s in zip(first, second):
#     distance += abs(f - s)
# print(distance)
# exit()

count_second = {}
score = 0
for num in second:
    count_second[num] = 1  + count_second.get(num, 0)

for num in first:
    if num in count_second:
        score += (num * count_second[num])
print(score)