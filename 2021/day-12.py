import pdb
from collections import defaultdict, Counter

BASIC_EXAMPLE = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

MIA_INPUT = """start-kc
pd-NV
start-zw
UI-pd
HK-end
UI-kc
pd-ih
ih-end
start-UI
kc-zw
end-ks
MF-mq
HK-zw
LF-ks
HK-kc
ih-HK
kc-pd
ks-pd
MF-pd
UI-zw
ih-NV
ks-HK
MF-kc
zw-NV
NV-ks"""

class Cave:
    def __init__(self, char):
        self.char = char
        self.connections = set()

    def add_connection(self, cave):
        self.connections.add(cave)

    def __repr__(self):
        return f'{self.char} connects to {self.connections}'


inputs = BASIC_EXAMPLE.split('\n')
caves = {}

for line in inputs:
    chars = line.split('-')
    # fetch or create cave
    if chars[0] not in caves.keys():
        cave = Cave(chars[0])
        caves[chars[0]] = cave
    else:
        cave = caves[chars[0]]

    if not chars[0] == 'end':
        cave.add_connection(chars[1])

    if not chars[1] in caves.keys():
        cave = Cave(chars[1])
        if not chars[1] == 'end' and not chars[0] == 'start':
            cave.add_connection(chars[0])
        caves[chars[1]] = cave
    else:
        if not chars[1] == 'end' and not chars[0] == 'start':
            caves[chars[1]].add_connection(chars[0])

# print(caves)
 
class Graph:
    def __init__(self):

        self.graph = defaultdict(list)
        self.path_count = 0
        self.visited_twice = (False, "")

    def __repr__(self):
        return str(self.graph)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def nodes_in_visited(self, list_of_nodes, visited):
        for node in list_of_nodes:
            if not node in visited:
                return False
        return True

    # def no_single_smallcave_twice(self, visited):
    #     lower = [node for node in visited if node.islower()]
    #     counter = Counter(lower)
    #     # print(counter)
    #     for count in counter.values():
    #         if count >= 2: return False
    #     return True

    def eligible_node(self, node, visited):
        if (node.isupper() and not self.nodes_in_visited(self.graph[node], visited)) or \
            (node.islower() and not self.visited_twice[0]):
            return True

    def dfs(self, path, node, end, visited):
        # if node not in visited:
        if self.eligible_node(node, visited):
            if node.islower() and node in visited:
                print("Visiting twice!")
                self.visited_twice = (True, node)
            visited.append(node)
            path.append(node)
            if node == end:
                self.path_count +=1
                print(f"Got to end: {path}")
            else:
                for neighbour in self.graph[node]:
                    self.dfs(path, neighbour, end, visited)
            if visited.pop() == self.visited_twice[1]: self.visited_twice = (False, "")
            path.pop()
 
    def start_pathfinding(self, v):
        visited = list()

        self.dfs([], v, 'end', visited)

# Instantiate the graph
g = Graph()
for cave in caves.values():
    for connection in cave.connections:
        g.addEdge(cave.char, connection) # I guess we use chars but we can lookup stuff from caves?

print(g)
 
print("Following is DFS from start to end")
g.start_pathfinding('start')
print(g.path_count)

