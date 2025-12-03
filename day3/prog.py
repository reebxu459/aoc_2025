def get_largest_joltage_1(batteries):
    batteries = ''.join(batteries)
    first, second = '0', '0'

    # first digit
    subst = batteries[:-1]
    mx = max(subst)
    idx = subst.find(mx)
    first = idx

    # second digit
    subst = batteries[idx+1:]
    mx = max(subst)
    sec_idx = subst.find(mx)
    second = sec_idx + idx + 1

    return batteries[first]+batteries[second]


def get_largest_joltage_2(batteries):
    batteries = ''.join(batteries)
    digits = []
    start = 0
    for i in range(11, -1, -1):
        end = len(batteries) if i == 0 else 0-i
        subst = batteries[start:end]
        mx = max(subst)
        idx = subst.find(mx)
        digits.append(subst[idx])
        start += idx+1
    return ''.join(digits)

f = open('input.txt').read().strip().split('\n')
banks = [list(bank) for bank in f]

res1 = res2 = 0
for line in banks:
    largest_joltage_1 = get_largest_joltage_1(line)
    largest_joltage_2 = get_largest_joltage_2(line)
    res1 += int(largest_joltage_1)
    res2 += int(largest_joltage_2)

print(res1)
print(res2)
