f = open('input.txt').read().strip().split('\n')

coords = list()
for line in f:
    coords.append([int(x) for x in line.split(',')])

def calc_rect_area(c1, c2):
    x = abs(c1[0] - c2[0]) + 1
    y = abs(c1[1] - c2[1]) + 1
    return x * y

def part1():
    cur_largest_area = 0
    for c1 in range(len(coords)):
        for c2 in range(c1, len(coords)):
            cur_largest_area = max(cur_largest_area, calc_rect_area(coords[c1], coords[c2]))

    print(cur_largest_area)

def part2():
    bounds = dict()  # row(y) : [min_x, max_x]

    for c in range(len(coords)):
        first = coords[c]
        second = coords[(c+1) % len(coords)]

        start_r = min(first[1], second[1])
        end_r   = max(first[1], second[1])
        start_c = min(first[0], second[0])
        end_c   = max(first[0], second[0])

        # horizontal edge
        if start_r == end_r:
            row = start_r
            if row not in bounds:
                bounds[row] = [start_c, end_c]
            else:
                bounds[row][0] = min(bounds[row][0], start_c)
                bounds[row][1] = max(bounds[row][1], end_c)

        # vertical edge
        else:
            for r in range(start_r, end_r + 1):
                if r not in bounds:
                    bounds[r] = [start_c, end_c]
                else:
                    bounds[r][0] = min(bounds[r][0], start_c)
                    bounds[r][1] = max(bounds[r][1], end_c)

    def check_uses_tiles(c1, c2):
        start_r = min(c1[1], c2[1])
        end_r   = max(c1[1], c2[1])
        start_c = min(c1[0], c2[0])
        end_c   = max(c1[0], c2[0])

        for r in range(start_r, end_r + 1):
            if r not in bounds:
                return False
            if start_c < bounds[r][0] or end_c > bounds[r][1]:
                return False
        return True

    cur_largest_area = 0
    for c1 in range(len(coords)):
        for c2 in range(c1, len(coords)):
            if check_uses_tiles(coords[c1], coords[c2]):
                cur_largest_area = max(cur_largest_area, calc_rect_area(coords[c1], coords[c2]))

    print(cur_largest_area)

part1()
part2()
