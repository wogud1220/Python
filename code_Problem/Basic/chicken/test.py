total = 0
with open('./data/chicken.txt', 'r') as f:

    for line in f:
        real_line = line.strip().split(': ')
        print(real_line[1])
        
        total += int(real_line[1])
        
print(total/31)