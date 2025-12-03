import string

def get_largest_joltage_1(batteries):
    batteries = ''.join(batteries)
    first, second = '0', '0'
    subst = batteries[:-1]
    for num in string.digits[::-1]:
        idx = subst.find(num)
        if idx != -1:
            first = idx
            break
    subst = batteries[idx+1:]
    for num in string.digits[::-1]:
        sec_idx = subst.find(num)
        if sec_idx != -1:
            second = sec_idx + idx + 1
            break
    return batteries[first]+batteries[second]


def get_largest_joltage_2(batteries):
    batteries = ''.join(batteries)
    digits = list()
    start = 0
    for i in range(11, -1, -1):
        end = len(batteries)
        if i != 0: end = 0-i
        subst = batteries[start:end]
        for num in string.digits[::-1]:
            idx = subst.find(num)
            if idx != -1: 
                digits.append(subst[idx])
                start += idx+1
                break
    return ''.join(digits)


f = open('input.txt')
banks = list()
for line in f:
    line = list(line.strip())
    banks.append(line)

res1 = res2 = 0
for line in banks:
    largest_joltage_1 = get_largest_joltage_1(line)
    largest_joltage_2 = get_largest_joltage_2(line)
    res1 += int(largest_joltage_1)
    res2 += int(largest_joltage_2)

print(res1)
print(res2)
