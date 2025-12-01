f = open('input.txt')

commands = list()

for line in f:
    line = line.split()
    commands.append(line)

cur_pos = 50
ctr = 0
MAX_POS = 100

for c in commands:
    c = c[0]
    direction = c[0]
    magnitude = int(c[1:])

    print(cur_pos, direction, magnitude, ctr)

    ctr += magnitude // MAX_POS
    magnitude -= (magnitude // MAX_POS) * MAX_POS

    if direction == 'L':
        if cur_pos - magnitude <= 0 and cur_pos != 0: ctr += 1
        cur_pos = (cur_pos - magnitude) % MAX_POS

    elif direction == 'R':
        if cur_pos + magnitude >= MAX_POS: ctr += 1
        cur_pos = (cur_pos + magnitude) % MAX_POS

print(ctr)
