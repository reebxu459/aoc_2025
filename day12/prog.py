f = open('input.txt').read().strip().splitlines()

shape_sizes = dict()
for i in range(0, 30, 5):
    shape_id = f[i][0]
    shape_tot = f[i+1] + f[i+2] + f[i+3]
    shape_sizes[shape_id] = shape_tot.count('#')

num_def_yes = 0
num_def_no = 0

for input in f[30:]:
    dimensions, *quantities = input.split()
    dimensions = [int(dimensions[:2]), int(dimensions[3:5])]
    quantities = [int(x) for x in quantities]
    
    area = dimensions[0] * dimensions[1]
    min_area_needed = sum([x * y for x, y in zip(shape_sizes.values(), quantities)])
    if area >= sum(quantities) * 9:
        num_def_yes += 1
    elif area < min_area_needed:
        num_def_no += 1

print(num_def_no, num_def_yes)










