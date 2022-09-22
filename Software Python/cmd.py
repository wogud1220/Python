def change_list(t):
    t[0] = t[0]
    t = t+[400, 500]
    return t
    
list = [100, 200, 300]
new_list =change_list(list)
print(list)
print(new_list)