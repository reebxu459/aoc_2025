def part_1():
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

        if direction == 'L':
            cur_pos = (cur_pos - magnitude) % MAX_POS
        elif direction == 'R':
            cur_pos = (cur_pos + magnitude) % MAX_POS
        
        if cur_pos == 0: ctr += 1
    print(ctr)


def part_2():
    f = open('input.txt')
    commands = list()
    for line in f:
        line = line.split()
        commands.append(line)

    cur_pos = 50
    ctr = 0
    MAX_POS = 100

    for c in commands:
        command = c[0]
        direction = command[0]
        magnitude = int(command[1:])
        
        ctr += magnitude // MAX_POS
        magnitude -= (magnitude // MAX_POS) * MAX_POS

        if direction == 'L':
            if cur_pos - magnitude <= 0 and cur_pos != 0: ctr += 1
            cur_pos = (cur_pos - magnitude) % MAX_POS
        elif direction == 'R':
            if cur_pos + magnitude >= MAX_POS: ctr += 1
            cur_pos = (cur_pos + magnitude) % MAX_POS
    print(ctr)


part_1()
part_2()
