import ast
import z3

f = open('input.txt').read().strip().splitlines()

def part1():
        
    def get_binary_strings(length):
        res = list()
        for i in range(2**length):
            bin_rep = bin(i)[2:]
            padded = bin_rep.zfill(length)
            res.append(padded)
        return res

    def meets_goal(goal, to_toggle):
        start = ['.'] * len(goal)
        for button in to_toggle:
            for idx in button:
                if start[idx] == '.': start[idx] = '#'
                else: start[idx] = '.'
        return ''.join(start) == goal

    res = 0
    for line in f:
        line = line.split()
        lights = line[0][1:-1]
        buttons = [ast.literal_eval(x) for x in line[1:-1]]
        buttons = [(x,) if type(x)==int else x for x in buttons]
        
        toggle_patterns = get_binary_strings(len(buttons))
        cur_min_buttons = len(buttons)
        for toggle_pattern in toggle_patterns:
            to_toggle = list()
            for ch, button in zip(toggle_pattern, buttons):
                if ch == '1': to_toggle.append(button)
            if meets_goal(lights, to_toggle):
                cur_min_buttons = min(cur_min_buttons, len(to_toggle))
        res += cur_min_buttons
    print(res)

def part2():
    res = 0
    for line in f:
        line = line.split()
        buttons = line[1:-1]
        buttons = [
            set([int(x) for x in button[1:-1].split(',')])
                for button in buttons
        ]
        joltages = line[-1]
        joltages = [int(x) for x in joltages[1:-1].split(',')]
        
        vars = [z3.Int('button'+str(i)) for i in range(len(buttons))]
        solver = z3.Optimize()
        solver.add(z3.And([var >= 0 for var in vars]))
        solver.add(z3.And([
            sum(vars[j] for j, button in enumerate(buttons) if i in button) == joltage
                for i, joltage in enumerate(joltages)
        ]))
        solver.minimize(sum(vars))
        solver.check()

        m = solver.model()
        for press in vars:
            res += m[press].as_long()

    print(res)

part1()
part2()
