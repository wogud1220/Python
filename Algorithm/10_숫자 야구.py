import random
secretLen = 4

secretList = random.sample(range(10), secretLen) # 0~9 중 4개 랜덤 선택
secret = ('')
for i in range(secretLen):
    secret += str(secretList[i]) # 문자열로 변환
#print (secret) # 테스트용

for chance in range(10,0,-1):
    while True:
        guess =input(('you have %d chance.' % chance)+ 'Guess my four digit number:')
        if len(guess) == secretLen and guess.isdigit():
            break

# 추론 숫자 분석
    strike = 0 # 스트라이크 초기화
    ball = 0 # 볼 초기화
    for i in range(secretLen): # 인자는 4
        if secret[i] == guess[i]:
            strike += 1 # 스트라이크 증가
        elif secret[i] in guess:
            ball += 1 # 볼 증가
    #print(secret, strike, ball) # 테스트용

    # 분석 결과 출력
    if strike == secretLen:
        print('You guessed my number!!')
        break
    if strike > 0:
        if ball > 0:
            print("%d strike(s) and %d ball(s)\n" % (strike, ball))
        else:
            print("%d strike(s)\n" % strike)
    else:
        if ball > 0:
            print ("%d ball(s)\n" % ball)
        else:
            print ("Out\n")
else:   #맨 위의 for range(10```) 에 해당하지 않으면
    print ('You failed to guess my number..')
