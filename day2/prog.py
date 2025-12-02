def has_dup_digit_1(num: int):
    num = str(num)
    return num[:len(num) // 2] == num[len(num) // 2:]

def has_dup_digit_2(num: int):
    num = str(num)
    length = len(num)
    for i in range(1, length):
        if length % i == 0:
            substring = num[:i]
            is_invalid = True
            for j in range(0, length-i+1, i):
                if substring != num[j:j+i]:
                    is_invalid = False
            if is_invalid: return True
    return False

def main():
    f = open('input.txt')
    ranges = list()
    for line in f:
        line = line.strip().split(',')
        for item in line: 
            if item != '': ranges.append(item)

    res1, res2 = list(), list()
    for r in ranges:
        r = r.split('-')
        first, second = int(r[0]), int(r[1])
        for i in range(first, second+1):
            if has_dup_digit_1(i): 
                res1.append(i)
            if has_dup_digit_2(i):
                res2.append(i)

    print(sum(res1))
    print(sum(res2))

main()
