i=1
dic={1:'바이킹',2:' 롤러코스터', 3: '자이로드롭', 4: '번지 점프', 5: '회전 목마',\
    6:'범퍼카', 7: '귀신의 집'}

print('⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⠇⠘⣿⣿⣿⡇⢰⣶⣶⡆⣿⣿\n\
⣿⣿⠋⣴⣷⡈⢿⣿⡇⢸⣿⣿⡇⣿⣿\n\
⣿⣯⣼⣿⣿⣿⣤⣿⣷⣶⣶⣶⣶⣿⣿\n\
⣿⣿⣿⡇⢸⣿⣿⣿⣿⠿⠇⢸⣿⣿⣿\n\
⣿⣿⣿⡇⢠⣤⣿⣿⣿⠿⠇⢸⣿⣿⣿\n\
⣿⣿⣿⣇⣸⣿⣿⣿⣿⣶⣆⣸⣿⣿⣿\n\
⣿⣿⠿⣋⣙⠻⣿⣿⣿⠟⣋⣙⠿⣿⣿\n\
⣿⡏⢰⣿⣿⣷⠈⣿⠃⣾⣿⣿⡆⢹⣿\n\
⣿⣷⣘⠻⠿⢋⣴⣿⣧⡙⠿⠟⣃⣾⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n')
number=int(input('안녕하세요 상명랜드에 오신 것을 환영합니다\n \n몇 명이서 오셨나요?\n')) # 정수만 입력
print('\n')

print(number,'명이서 오셨군요~!!\n')
number=int(number)
print('15세 이상은 3만원, 15세 미만 아이로 취급하여 만원입니다.\n')
child=input('혹시 그 중에 아이가 있으신가요? 네 or 아니오\n')  #네 또는 아니오만 입력하기
print('\n')
if(child=='네'):
    child1=input('아이 1명당 10% 할인이 됩니다. 아이가 몇 명인가요?\n')  #아이의 인원 정수 입력
    child1=int(child1)
    print('\n')
    print('아이가',child1,'명 이므로',child1*10,'% 할인이 됩니다.')
    sale=float(child1*10/100)
    print('가격은 총',(number-child1)*30000 + child1*10000,'원에서 할인하여',
    ((number-child1)*30000 + child1*10000) -
    int((((number-child1)*30000 + child1*10000)*child1*10/100)),'입니다.\n')
    print('===============================================================\n\
===============================================================\n\n')
    print('상명랜드에 오신 것을 다시 한번 환영합니다~!\n\
 1.바이킹\n 2.롤러코스터\n 3.자이로드롭\n 4.번지 점프\n 5.회전 목마\n\
 6.범퍼카\n 7.귀신의 집\n 등 다양한 놀이기구가 있습니다!!\n')
    nol_choice=[]
    print('놀이기구 탑승은 최대 4번까지 가능하므로 타고 싶은 놀이기구를 4개만 선택\
해주세요~~!\n')
    for j in range(1,5,1):
        nol_turn=int(input('%d번째로 타고 싶은 놀이기구의 번호를 입력하고 엔터를 누르세요\n' %j)) #번호 입력하기
        nol_choice.append(nol_turn)
        print(nol_turn,dic[nol_turn],'\n','순서 :',nol_choice)
        
    if(1 <= child1 and ((nol_choice[0] or nol_choice[1] or nol_choice[2] or nol_choice[3])
                        ==1 or 2 or 3 or 4)):
        print('죄송하지만 고객님이 타시려는 놀이기구들은 키와 몸무게 제한이 있는\
놀이기구 입니다.\n 키:100cm 초과, 몸무게는 25kg 초과할 것\n 아이의 키와 몸무게를 입력해주시겠어요?')
        while(i<=child1):
            height=float(input('%d째 아이의 키: '%i))            #키, 몸무게 정수 입력
            weight=float(input('%d째 아이의 몸무게: '%i))
            if(height <= 100 or weight <= 25):
                print('아이의 신체조건이 맞지 않습니다. 다시 입력해주세요.')
                continue
            i=i+1
        else:
            print('\n아이들의 신체조건을 모두 입력받았습니다. 가는 길을 알려드리겠습니다.')
else:
    print('아이가 없으시군요~ 알겠습니다.\n')
    print('가격은 총 %d입니다' %(number*30000))
    print('\n\n\n===========================================================\n')
    print('상명랜드에 오신 것을 다시 한번 환영합니다~!\n\
 1.바이킹\n 2.롤러코스터\n 3.자이로드롭\n 4.번지 점프\n 5.회전 목마\n\
 6.범퍼카\n 7.귀신의 집\n 등 다양한 놀이기구가 있습니다!!\n')
    nol_choice=[]
    print('놀이기구 탑승은 최대 4번까지 가능하므로 타고 싶은 놀이기구를 4개만 선택\
해주세요~~!\n')
    for j in range(1,5,1):
        nol_turn=int(input('%d번째로 타고 싶은 놀이기구의 번호를 입력하고 엔터를 누르세요\n' %j))
        nol_choice.append(nol_turn)
        print(nol_turn,dic[nol_turn],'\n','순서 :',nol_choice)

print('\n\n\n===========================================================\n')
print('\n\n네 여기 약도 그려드렸습니다. 받으시고 즐거운 시간 되시길 바랍니다~')


import turtle
t=turtle.Turtle()

s=turtle.Screen()
s.setup(width = 1600, height = 850)
image="smuuu.gif"   #배경
image2="smuu.gif"  #수뭉이
s.bgpic(image)
s.addshape(image)
s.addshape(image2)


t.hideturtle()
t.penup()
t.setpos(0,-190)
t.pendown()
t.write("매표소 (현재위치)", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(200,-250)
t.pendown()
t.write("바이킹", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(250,0)
t.pendown()
t.write("롤러코스터", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(150,200)
t.pendown()
t.write("자이로드롭", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-100,250)
t.pendown()
t.write("번지점프", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-250,150)
t.pendown()
t.write("회전 목마", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-400,0)
t.pendown()
t.write("범퍼카", move=False, align="center", font=("arial",20,"bold"))

t.penup()
t.setpos(-350,-250)
t.pendown()
t.write("귀신의 집", move=False, align="center", font=("arial",20,"bold"))
t.penup()

t.setpos(0,-190)
t.shape(image2)
t.pendown()
t.showturtle()

t.pensize(3)

k=0
n=0
while(n<4):
    t.color('blue')
    if(nol_choice[k]==1):
        t.goto(200,-250)
    elif(nol_choice[k]==2):
        t.goto(250,0)
    elif(nol_choice[k]==3):
        t.goto(150,200)
    elif(nol_choice[k]==4):
        t.goto(-100,250)
    elif(nol_choice[k]==5):
        t.goto(-250,150)
    elif(nol_choice[k]==6):
        t.goto(-400,0)
    elif(nol_choice[k]==7):
        t.goto(-350, -250)
    t.color('red')
    t.write(n+1, move=False, align="left", font=("arial",30,"bold"))
    k+=1
    n+=1

    
#print('네 그러면 먼저', dic[(nol_want)], '쪽으로 안내해드리겠습니다.')'''





