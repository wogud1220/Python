v= [1, 4, 9,  16, 25, 36, 49, 64, 81]

n= int(input('찾을 값은?'))

start=0
end =len(v)-1
print(len(v))

while start<=end:
    mid=(start +end)//2
    if(n==v[mid]):
        print('%d는 리스트에서 %d번째 순서에 있습니다.'% (n, mid+1))
        break
    elif n>v[mid]:
        start=mid+1
    else:
        end = mid -1

else:
    print('%d를 리스트에서 찾을 수 없습니다.'%n)

