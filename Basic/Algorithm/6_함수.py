def addition(n1,n2):
    print('%d + %d =%d' %(n1, n2, n1+n2))
def subtraciton(n1,n2):
    print('%d - %d =%d' %(n1, n2, n1-n2))

num1 = int(input('첫번째 정수 입력: '))

num2 = int(input('두번째 정수 입력 : '))
op = input('연산자선택 (+, -): ')
if op == '+':
    addition(num1,num2)
else :
    subtraciton(num1,num2)
