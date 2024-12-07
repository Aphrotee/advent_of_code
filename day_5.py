from collections import defaultdict

def build_graph(pairs):
    adj = defaultdict(set)

    for x, y in pairs:
        adj[x].add(y)

    return adj

def build_graph_list(pairs):
    adj = defaultdict(list)

    for x, y in pairs:
        adj[x].append(y)

    return adj

def check_order(graph, order):
    
    def dfs(index):
        if index == len(order):
            return True

        if order[index] in graph[order[index - 1]]:
            if dfs(index + 1):
                return True
        return False
    if order[0] in graph:
        return dfs(1)
    return False


def reorder(graph, nodes):
    right_order = []

    def dfs(index, visited, to_visit):
        if index == len(nodes):
            # right_order = path
            return True
        
        for child in graph[right_order[-1]]:
            if child in to_visit:
                visited.add(child)
                to_visit.remove(child)
                right_order.append(child)
                if dfs(index + 1, visited, to_visit):
                    return True
                right_order.pop()
                visited.remove(child)
                to_visit.add(child)

        
        return False
    to_visit = set(nodes)
    for node in nodes:
        to_visit.remove(node)
        right_order.append(node)
        if dfs(1, set([node]), to_visit):
            return right_order
        to_visit.add(node)
        right_order.pop()
    return right_order
    
pairs = []
while True:
    line = input()
    if line == '':
        break
    pair = tuple(map(int, line.split('|')))
    pairs.append(pair)

graph = build_graph(pairs)
graph_list = build_graph_list(pairs)


answer = 0
# while True:
#     line = input()
#     if line == '':
#         break
#     order = list(map(int, line.split(',')))
#     length = len(order)
#     if check_order(graph, order):
#         answer += order[(length // 2)]

while True:
    line = input()
    if line == '':
        break
    order = list(map(int, line.split(',')))
    length = len(order)
    if not check_order(graph, order):
        reordered = reorder(graph_list, order)
        answer += reordered[(length // 2)]
print(answer)