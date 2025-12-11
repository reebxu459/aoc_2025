from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(cur_node, dac_found=False, fft_found=False):
    if cur_node == 'out': return dac_found and fft_found
    elif cur_node == 'dac': dac_found = True
    elif cur_node == 'fft': fft_found = True
    return sum([dfs(x, dac_found, fft_found) for x in G[cur_node]])

f = open('input.txt').read().strip().splitlines()
G = dict()
for line in f:
    node, *outputs = line.split()
    node = node[:-1]
    G[node] = outputs

print(dfs('you', True, True))
print(dfs('svr'))
