# 순방향 추론
def fire_expert(short):
   # 주위가 뜨겁고 연기가 나면 불이난다
   if "B" in short and "C" in short: 
      short.append("D")
    # 알람이 울리면 연기가 난다
   if "A" in short : 
      short.append("C")
    # 불이나면 소방서에 신고한다
   if "D" in short :    
      short.append("E")

short = ["A", "B"]
print(short)

fire_expert(short)
# [A,B,C]
if "E" in short : print("소방서에 신고한다")
fire_expert(short)
#[A,B,C,D,E]
if "E" in short : print("소방서에 신고한다")
# 여러번 돌려야한다. 






def a(short):

    if "A" in short and "B" in short:

        short.append("C")

        cf = min(0.8,0.1)*0.7

        print(cf)

    if "D" in short:

        short.append("E")

        cf = (0.7-0.1)*0.6

        print(cf)

    if "F" in short:

        short.append("G")

        cf = 1.0

        print(cf)

    if "H" in short:

        cf = (0.8-0.2)*0.6

        print(cf)

    if "B" in short:

        short.append("I")

        cf =1

        print(cf)

short = ["A","B","H","F"]

print(short)

a(short)

if "C" in short : print("감기이다")