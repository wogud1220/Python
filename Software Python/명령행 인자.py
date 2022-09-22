import sys
print('명령행 인자의 수:', len(sys.argv))
print('명령행 인자의 목록:', str(sys.argv))
print('명령행 인자 3개의 합:', int(sys.argv[1])+ int(sys.argv[2])+int(sys.argv[3]))