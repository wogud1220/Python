dec=5
num = int(input("제가 생각하는 1부터 20사이의 정수중 하나를 맞추어 보세요\n"))
if num >dec:
    print('추측한 값이 큽니다.')
elif num<dec:
    print('추측한 값이 작습니다.')
else:
    print('맞습니다!')
