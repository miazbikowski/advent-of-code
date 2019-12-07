print("Advent of Code - Day 6")

f = open("input6", "r")

orbits = []
for x in f:
    orbits.append(x)

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

class Node:
    def __init__(self, identifier):
        self.id = identifier
        self.orbits = None
        self.orbitted_by = None

    def add_orbit(self, orbit):
        self.orbits = orbit

    def add_orbited_by(self, orbit):
        self.orbitted_by = orbit

class OrbitsGraph:
    def __init__(self):
        self.nodes = {}

    @staticmethod
    def parse_orbit_pair(orbital_pair):
        # parses 'COM)B' as COM is orbiter and B is orbitee
        return orbital_pair.split(')')

    def create_or_update_nodes(self, orbital_pair):
        orbitee, orbiter = self.parse_orbit_pair(orbital_pair)
        if orbitee not in self.nodes:
            self.nodes[orbitee] = Node(orbitee)
        if orbiter not in self.nodes:
            self.nodes[orbiter] = Node(orbiter)

        self.nodes[orbiter].add_orbit(self.nodes[orbitee])
        self.nodes[orbitee].add_orbited_by(self.nodes[orbiter])

    def populate_tree(self, test_orbits):
        for orbital_pair in test_orbits:
            self.create_or_update_nodes(orbital_pair)

    def checksum_orbits(self):
        total_count = 0
        for id, node in self.nodes.items():
            total_count += self.count_orbits_for_node(node)

        return total_count

    def count_orbits_for_node(self, node):
        count = 0
        while node.orbits != None:
            count += 1
            node = node.orbits
        return count


assert OrbitsGraph.parse_orbit_pair('COM)B') == ['COM', 'B']

orbits_tree = OrbitsGraph()
orbits_tree.populate_tree(test_orbits)
print(orbits_tree.checksum_orbits())

orbits_tree = OrbitsGraph()
orbits_tree.populate_tree(orbits)
print(orbits_tree.checksum_orbits())