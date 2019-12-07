import collections

print("Advent of Code - Day 6")

with open('input6') as f:
  orbits = [ orbit_text for orbit_text in f.read().rstrip().split('\n')]

test_orbits = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)L',
]

class Graph:
    def __init__(self, orbits):
        self.graph = collections.defaultdict(list)
        for orbital_pair in orbits:
            orbitee, orbiter = self.parse_orbit_pair(orbital_pair)
            # in test case COM is orbitee, B is orbiter
            self.graph[orbitee].append(orbiter)
            self.graph[orbiter].append(orbitee) # make graph undirected

    @staticmethod
    def parse_orbit_pair(orbital_pair):
        # parses 'COM)B' as COM is orbiter and B is orbitee
        return orbital_pair.split(')')[0], orbital_pair.split(')')[1]

    def flatten(self, l, output=None):
        if output is None:
            output = []
        for i in l:
            if isinstance(i, list):
                self.flatten(i, output)
            else:
                output.append(i)
        return output

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath: return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_paths_to_start(self):
        paths = []
        for place in self.graph.keys():
            # print("Finding all paths to %s" % place)
            place_paths = self.find_all_paths('COM', place)
            # print(place_paths)
            paths.extend(place_paths)
        return paths

    def count_orbits(self):
        paths = self.find_paths_to_start()
        print(paths)
        return sum(len(path) - 1 for path in paths)

# print(Graph(test_orbits).graph)
# print(Graph(test_orbits).find_all_paths('COM', 'L'))
print(Graph(test_orbits).count_orbits())

print(Graph(orbits).count_orbits())