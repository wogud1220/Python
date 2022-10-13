import turtle as t

print(number)
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
t.setpos(300,-150)
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
t.setpos(-400,50)
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
