f = open('input.txt').read().strip().split('\n')
grid = [list(line) for line in f]

def part1():
    # draw the lines
    for r in range(len(grid)-1):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S' or grid[r][c] == '|':
                if grid[r+1][c] == '^':
                    if c > 0: grid[r+1][c-1] = '|'
                    if c < len(grid[0])-1: grid[r+1][c+1] = '|'
                else:
                    grid[r+1][c] = '|'
    # count the occurences of:
    # |
    # ^
    cnt = 0
    for r in range(len(grid)-1):
        for c in range(len(grid[0])):
            if grid[r][c] == '|' and grid[r+1][c] == '^': 
                cnt += 1
    print(cnt)

def part2():
    # keep track of the number of beams in the multiverse in each column
    beam_count = [0] * len(grid[0])

    for r in range(len(grid)-1):
        for c in range(len(grid[0])):
            # start
            if grid[r][c] == 'S':
                beam_count[c] = 1
                grid[r+1][c] = '|'
            if grid[r][c] == '|':
                if grid[r+1][c] == '^':
                    if c > 0: 
                        grid[r+1][c-1] = '|'
                        beam_count[c-1] += beam_count[c]
                    if c < len(grid[0])-1: 
                        grid[r+1][c+1] = '|'
                        beam_count[c+1] += beam_count[c]
                    beam_count[c] = 0
                else:
                    grid[r+1][c] = '|'
    print(sum(beam_count))

part1()
part2()
