# 무단횡단을 한다

# 사실 A: 좌우를 살핀다.
# 사실 B: 신호등이 없다.
# 사실 C: 횡단보도가 없다.
# 사실 D: 돌아다니는 차가 없다.
# 사실 E: 건넌다.

# 규칙 1: 횡단보도가 없고 신호등이 없으면 좌우를 살핀다.
# B & C -> A

# 규칙 2: 좌우를 살피고 차가 없으면 건넌다.
# A & D -> E

def fire_expert(short):
   if "B" in short and "C" in short: 
      short.append("A")
   if "A" in short and "D" in short: 
      short.append("E")

short = ["B", "C", "D"]
print(short)

fire_expert(short)
if "E" in short : print("건넌다.")

fire_expert(short) # B, C, A
if "E" in short : print("건넌다.")
