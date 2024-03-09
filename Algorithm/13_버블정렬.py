v = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
print('정렬 전', v, '\n')
print(len(v))

for i in range(len(v)-1, 0, -1):
    for j in range(0,i):
        if v[j]>v[j+1]:
            v[j], v[j+1] = v[j+1], v[j]

print('정렬 후:',v)



