import turtle
#t=turtle.Turtle()

number=int(input('안녕하세요 놀이공원에 오신 것을 환영합니다. \n몇 명이서 오셨나요?'))
print(number,'명이서 오셨군요~!!\n\n')

print('남자 성인은 3만원 여자 성인은 2만원입니다.')

child=(input('아이가 있으신가요? 네 or 아니오\n'))

if(child=='네'):
    child1=int(input('아이 1명당 10% 할인이 됩니다. 아이가 몇 명인가요?\n'))
    print('아이가',child1,'명 이므로',child1*10,'% 할인이 됩니다.')
   # print('총
