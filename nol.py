
        
dic={1:'바이킹',2:' 롤러코스터', 3: '자이로드롭', 4: '번지 점프', 5: '회전 목마',\
    6:'범퍼카', 7: '귀신의 집'}
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
    print('상명랜드에 오신 것을 환영합니다~!\n\
    1.바이킹\n 2.롤러코스터\n 3.자이로드롭\n 4.번지 점프\n 5.회전 목마\n\
    6.범퍼카\n 7.귀신의 집\n 중에서 제일 먼저 타고 싶은 놀이기구의 번호를 입력하세요.\n')
    nol_sunseo=[]
    for j in range(4):
        nol_turn=int(input('타고 싶은 놀이기구를 입력하고 엔터를 누르세요\n'))
        nol_sunseo.append(nol_turn)
        print(nol_sunseo)

    if(1 <= child1 and (nol_sunseo[0]==1 or 2 or 3 or 4)):
        print('죄송하지만 고객님이 타시려는 놀이기구들은 키와 몸무게 제한이 있는\
놀이기구 입니다.\n 키:100cm 초과, 몸무게는 25kg 초과할 것\n 아이의 키와 몸무게를 입력해주시겠어요?')
        for i in range(1,child1+1,1):
            height=int(input('%d째 아이의 키: '%i))
            weight=int(input('%d째 아이의 몸무게: '%i))
            if(height <= 100 or weight <= 25):
                print('아이의 신체조건이 맞지 않습니다.')
                continue;
            else:
                print('\n아이들의 신체조건이 탑승조건에 만족합니다.')
    

                
elif(child=='아니오'):
    print('아이가 없으시군요~ 알겠습니다.\n')

import turtle as t

t.hideturtle()
t.penup()
t.setpos(0,-390)
t.pendown()
t.write("매표소 (현재위치)", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(300,-350)
t.pendown()
t.write("바이킹", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(300,-100)
t.pendown()
t.write("롤러코스터", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(200,200)
t.pendown()
t.write("자이로드롭", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-100,300)
t.pendown()
t.write("번지점프", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-350,200)
t.pendown()
t.write("회전 목마", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-300,50)
t.pendown()
t.write("범퍼카", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-350,-200)
t.pendown()
t.write("귀신의 집", move=False, align="center", font=("arial",20,"bold"))
t.penup()

t.setpos(0,-390)
t.shape('circle')
t.pendown()
t.showturtle()

t.pensize(3)
n=0
k=0


while(n<4):
    if(nol_sunseo[k]==1):
        t.goto(300,-350)
    elif(nol_sunseo[k]==2):
        t.goto(300,-350)
    elif(nol_sunseo[k]==3):
        t.goto(300,-100)
    elif(nol_sunseo[k]==4):
        t.goto(200,200)
    elif(nol_sunseo[k]==5):
        t.goto(-100,300)
    elif(nol_sunseo[k]==6):
        t.goto(-350,200)
    elif(nol_sunseo[k]==7):
        t.goto(-300,-200)
    n+=1
    k+=1
