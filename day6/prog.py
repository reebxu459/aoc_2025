import math

f = open('input.txt').read().strip().split('\n')

def apply_op(nums, op:str):
    if op == '*':
        return math.prod(nums)
    if op == '+':
        return sum(nums)

def part_1():
    num_problems = len(f[0].split())
    problems = [[] for _ in range(num_problems)]
    for i in range(len(f)-1):
        line = f[i].split()
        for j in range(num_problems):
            problems[j].append(int(line[j]))
    operations = f[-1].split()

    res = 0
    for i in range(num_problems):
        res += apply_op(problems[i], operations[i])
    print(res)

def part_2():
    operation_line = f[-1]
    num_num_lines = len(f)-1

    res = 0
    l, r = 0, 1
    while r < len(operation_line):
        if operation_line[r] != ' ':
            op = operation_line[l]
            nums = list()
            for i in range(r-2, l-1, -1):
                cur_num = list()
                for j in range(num_num_lines):
                    if f[j][i] != ' ': cur_num.append(f[j][i])
                nums.append(int(''.join(cur_num)))
            res += apply_op(nums, op)
            l = r
            r += 1
        else:
            r += 1
    # last number
    op = operation_line[l]
    nums = list()
    for i in range(r+1, l-1, -1):
        cur_num = list()
        for j in range(num_num_lines):
            if f[j][i] != ' ': cur_num.append(f[j][i])
        nums.append(int(''.join(cur_num)))
    res += apply_op(nums, op)

    print(res)

part_1()
part_2()