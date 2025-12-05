f = open('input.txt').read().strip().split('\n')

fresh_ranges = ingredients = list()
for i in range(len(f)):
    if not f[i]:
        fresh_ranges = [r for r in f[:i]]
        ingredients = [i for i in f[i+1:]]

for i in range(len(fresh_ranges)):
    fresh_ranges[i] = fresh_ranges[i].split('-')
    fresh_ranges[i][0] = int(fresh_ranges[i][0])
    fresh_ranges[i][1] = int(fresh_ranges[i][1])

def is_spoiled(ingredient):
    for r in fresh_ranges:
        if r[0] <= ingredient <= r[1]:
            return False
    return True

def part1():
    res = 0
    for i in ingredients:
        if not is_spoiled(int(i)): res += 1
    print(res)

def part2():
    fresh_ranges.sort(key=lambda x: x[0])
    merged_ranges = [range(fresh_ranges[0][0], fresh_ranges[0][1]+1)]

    for start, end in [(r[0], r[1]) for r in fresh_ranges]:
        current_start, current_end = merged_ranges[-1][0], merged_ranges[-1][-1]
        if start <= current_end:
            merged_ranges[-1] = range(current_start, max(current_end, end)+1)
        else:
            merged_ranges.append(range(start, end+1))
    print(sum(len(r) for r in merged_ranges))

part1()
part2()
