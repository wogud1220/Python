def find_min_idx(a, start):
    n = len(a)
    min_idx= start
    for i in range(start+1, n):
        if a[i] < a[min_idx]:
            min_idx =i
    return min_idx


v = [2, 4, 5, 1, 3]
for i in range(len(v)-1):
    min_idx = find_min_idx(v, i)
    v[i], v[min_idx] = v[min_idx], v[i]

print(v)