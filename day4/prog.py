f = open('input.txt').read().strip().split('\n')

grid = [list(line) for line in f]

TP = '@'

def part1():
    accessible_tp_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != TP: continue
            tp_count = 0
            # corners
            if r > 0 and c > 0 and grid[r-1][c-1] == TP: tp_count += 1
            if r > 0 and c < len(grid[0])-1 and grid[r-1][c+1] == TP: tp_count += 1
            if r < len(grid)-1 and c > 0 and grid[r+1][c-1] == TP: tp_count += 1
            if r < len(grid)-1 and c < len(grid[0])-1 and grid[r+1][c+1] == TP: tp_count += 1
            # sides
            if r > 0 and grid[r-1][c] == TP: tp_count += 1
            if r < len(grid)-1 and grid[r+1][c] == TP: tp_count += 1
            if c > 0 and grid[r][c-1] == TP: tp_count += 1
            if c < len(grid[0])-1 and grid[r][c+1] == TP: tp_count += 1

            if tp_count < 4: 
                accessible_tp_count += 1
    print(accessible_tp_count)

def part2():
    total_removed_tp = 0
    while True:
        accessible_tp_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != TP: continue
                tp_count = 0
                # corners
                if r > 0 and c > 0 and grid[r-1][c-1] == TP: tp_count += 1
                if r > 0 and c < len(grid[0])-1 and grid[r-1][c+1] == TP: tp_count += 1
                if r < len(grid)-1 and c > 0 and grid[r+1][c-1] == TP: tp_count += 1
                if r < len(grid)-1 and c < len(grid[0])-1 and grid[r+1][c+1] == TP: tp_count += 1
                # sides
                if r > 0 and grid[r-1][c] == TP: tp_count += 1
                if r < len(grid)-1 and grid[r+1][c] == TP: tp_count += 1
                if c > 0 and grid[r][c-1] == TP: tp_count += 1
                if c < len(grid[0])-1 and grid[r][c+1] == TP: tp_count += 1

                if tp_count < 4: 
                    accessible_tp_count += 1
                    grid[r][c] = '.'
        if accessible_tp_count == 0: break
        total_removed_tp += accessible_tp_count
    print(total_removed_tp)

part1()
part2()
