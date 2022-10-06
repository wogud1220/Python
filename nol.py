import turtle
#t=turtle.Turtle()

number=int(input('안녕하세요 놀이공원에 오신 것을 환영합니다\n \n몇 명이서 오셨나요?\n'))
print(number,'명이서 오셨군요~!!\n\n')
number=int(number)
print('15세 이상은 3만원, 15세 미만 아이로 취급하여 만원입니다.\n')


child=input('혹시 그 중에 아이가 있으신가요? 네 or 아니오\n')
if(child=='네'):
    child1=input('아이 1명당 10% 할인이 됩니다. 아이가 몇 명인가요?\n')
    child1=int(child1)
    print('아이가',child1,'명 이므로',child1*10,'% 할인이 됩니다.')
    sale=float(child1*10/100)
    print('가격은 총',(number-child1)*30000 + child1*10000,'원에서 할인하여',
    ((number-child1)*30000 + child1*10000) -
    int((((number-child1)*30000 + child1*10000)*child1*10/100)),'입니다.\n\n')
else:
    print('아이가 없으시군요~ 알겠습니다.')
dic={1:'바이킹',2:' 롤러코스터', 3: '자이로드롭', 4: '번지 점프', 5: '회전 목마',\
     6:'범퍼카', 7: '귀신의 집'}
nol_want=int(input('상명랜드에 오신 것을 환영합니다~!\n\
 1.바이킹\n 2.롤러코스터\n 3.자이로드롭\n 4.번지 점프\n 5.회전 목마\n\
 6.범퍼카\n 7.귀신의 집\n 중에서 타고 싶은 놀이기구의 번호를 입력하세요.\n'))

if(1 <= child1 and (nol_want==1 or 2 or 3 or 4)):
    int(input('죄송하지만 고객님이 타시려는 놀이기구들은 키와 몸무게 제한이 있는\
놀이기구 입니다 아이의 키와 몸무게를 입력해주시겠어요?'))
print('네 그러면 먼저', dic[(nol_want)], '쪽으로 안내해드리겠습니다.')


# 자녀의 키, 몸무게, 기구제한
# 터틀 약도 (건물, 시간,)
