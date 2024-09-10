def fun():
    print('fun() in A.py')
print('Hello A!')
if (__name__=='__main__'):
    print('A.py 직접 실행')
else:
    print('A.py가 임포트되어 실행')
