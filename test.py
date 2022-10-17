nol_want=int(input('상명랜드에 오신 것을 환영합니다~!\n\
    1.바이킹\n 2.롤러코스터\n 3.자이로드롭\n 4.번지 점프\n 5.회전 목마\n\
    6.범퍼카\n 7.귀신의 집\n 중에서 제일 먼저 타고 싶은 놀이기구의 번호를 입력하세요.\n'))

nol_sunseo=[]
for j in range(4):
    nol_turn=int(input('타고 싶은 놀이기구를 입력하고 엔터를 누르세요\n'))
    nol_sunseo.append(nol_turn)

print(nol_sunseo)
