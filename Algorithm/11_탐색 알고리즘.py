v= [5, 7, 50, 70, 500, 700]
n=int(input('찾을 값은?'))
for i in range(len(v)):
    if v[i] == n:
        print('%d는 리스트에서 %d번째 순서에 있습니다.'%(n,i+1))
        break

else:
    print('%d를 리스트에서 찾을 수 없습니다.' %n)

