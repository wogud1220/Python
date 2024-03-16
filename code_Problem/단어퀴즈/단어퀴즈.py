
# with open('./vocabulary.txt', 'w') as f:
#     while True:
#         eng_word = input('영어 단어를 입력하세요: ')
#         if eng_word == 'q':
#             break
#         kor_word = input('한국어 뜻을 입력하세요: ')
#         f.write(eng_word + ': ')
#         f.write(kor_word + '\n')

# with open('./vocabulary.txt', 'r') as f:
#     for line in f:
#         line=line.strip().split(': ')
#         kor_answer = input(line[1]+': ')
#         if kor_answer == line[0]:
#             print('맞았습니다!\n')
#         else:
#             print('아쉽습니다. 정답은 {}입니다.\n'.format(line[0]))


import random

dictionary = {}
words = 0
with open('./vocabulary.txt', 'r') as f:
    for line in f:
        line=line.strip().split(': ')
        a = line[0][:]
        dictionary[a]=line[1][:]
        words+=1

b = list(dictionary.items())
random.shuffle(b)

for i in range(words):
    answer = input(b[i][1] + ': ')
    if answer == b[i][0]:
        print('맞았습니다!\n')
    elif answer == 'q':
        break
    else:
        print('틀렸습니다. 정답은 {}입니다.\n'.format(b[i][0]))

