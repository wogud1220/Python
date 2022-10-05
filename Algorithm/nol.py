import turtle
#t=turtle.Turtle()

number=int(input('안녕하세요 놀이공원에 오신 것을 환영합니다. \n몇 명이서 오셨나요?\n'))
print(number,'명이서 오셨군요~!!\n\n')
number=int(number)
print('15세 이상은 3만원, 15세 미만 아이는 만원입니다.\n')


child=input('혹시 그 중에 아이가 있으신가요? 네 or 아니오\n')

if(child=='네'):
    child1=input('아이 1명당 10% 할인이 됩니다. 아이가 몇 명인가요?\n')
    child1=int(child1)
    print('아이가',child1,'명 이므로',child1*10,'% 할인이 됩니다.')
    sale=float(child1*10/100)
    print('가격은 총',(number-child1)*30000 + child1*10000,'원에서 할인하여',
    ((number-child1)*30000 + child1*10000) -int((((number-child1)*30000 + child1*10000)*child1*10/100)),'입니다.')
else:
    print('아이가 없으시군요~ 알겠습니다.')



# 기구 리스트 생성
# 자녀의 키, 몸무게, 기구제한

