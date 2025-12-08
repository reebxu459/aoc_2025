import math
from collections import Counter

f = open('input.txt').read().strip().split('\n')
LENGTH = len(f)

def get_straight_line_distance(coord_1, coord_2):
    return math.dist(coord_1, coord_2)

class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        parent = self.find(self.parents[x])
        self.parents[x] = parent
        return parent

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.sizes[a] <= self.sizes[b]:
            self.parents[a] = b
            self.sizes[b] += self.sizes[a]
        else:
            self.parents[b] = a
            self.sizes[a] += self.sizes[b]

junction_coords = list()
for line in f:
    junction_coords.append(tuple(int(x) for x in line.split(',')))

dists = [
    (i, j, get_straight_line_distance(junction_coords[i], junction_coords[j]))
    for i in range(LENGTH)
    for j in range(i+1, LENGTH)
]

dists.sort(key=lambda x: x[2])


def part1():
    uf = UnionFind(LENGTH)
    for i in range(LENGTH):
        j1 = dists[i][0]
        j2 = dists[i][1]
        uf.union(j1, j2)

    sizes = Counter()
    for i in range(LENGTH):
        sizes[uf.find(i)] += 1

    sum_top_3 = [s[1] for s in sizes.most_common(3)]

    print(sum_top_3)
    print(math.prod(sum_top_3))

def part2():
    uf = UnionFind(LENGTH)
    for i in range(len(dists)):
        j1 = dists[i][0]
        j2 = dists[i][1]
        uf.union(j1, j2)
        if uf.sizes[uf.find(j1)] == LENGTH:
            print(junction_coords[j1][0] * junction_coords[j2][0])
            break


part1()
part2()