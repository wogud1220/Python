#service, delicious, Tip, Result는 이산데이터로 가정

# 규칙 1. if 미세먼지가 적다 OR 초미세먼지가 적다
# 	=> 창문을 여는 시간을 길게 한다.
# 규칙 2. 미세먼지가 적당하다
# 	=> 창문을 적당히 연다.
# 규칙 3. 미세먼지가 많다 OR 초미세먼지가 많다
# 	=> 창문을 여는 시간을 짧게 한다.


#미세먼지가 많다.
#초미세먼지가 많다.
service1 =   [1, 0.95, 0.8, 0.85, 0.8, 0.7, 0.4, 0.2, 0.1, 0.05]
delicious1 = [1, 1.0, 0.8, 0.9, 0.6, 0.3, 0.1, 0.1, 0.1, 0.01]
Tip1    =    [0.0, 0.0, 0.2, 0.2, 0.3, 0.4, 0.6, 0.8, 0.9, 0.9]

Result1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0, 10) :
    Result1[i] = min(max(service1[1], delicious1[6]), Tip1[i])
print(Result1)

#미세먼지가 적당하다
service2=[0, 0.2, 0.3, 0.4, 0.5, 1.0, 0.5, 0.4, 0.3, 0.1] 
Tip2=[0.0, 0.0, 0.2, 0.3, 0.6, 1.0, 0.6, 0.3, 0.2, 0.0] 
Result2=[0.0, 0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(0, 10) :
    Result2[i] = min(service2[1], Tip2[i])
print(Result2)

#미세먼지가 적다
#초미세먼지가 적다
service3=   [0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0]
delicious3= [0, 0.1, 0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.9, 1.0] 
Tip3=       [0.0, 0.1, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 0.9]
Result3= [0.0, 0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for i in range(0, 10) :
    Result3[i] = min(max(service3[1], delicious3[6]),Tip3[i])
print(Result3)

reverse_fuzzy = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0, 10) :
    reverse_fuzzy[i] = max(Result1[i], Result2[i], Result3[i])
print(reverse_fuzzy)
T1=0
T2=0
for i in range(0, 10):
    T1 += i*reverse_fuzzy[i]
    T2 += reverse_fuzzy[i]
print(T1)
print(T2)
T3= round(T1/T2)
print (reverse_fuzzy[T3])



