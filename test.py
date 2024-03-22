import pandas as pd
import random

stu_data = pd.read_csv('./StudentsPerformance.csv')
stu_data = pd.DataFrame(stu_data)

# 6. 시험 준비 과정을 완료 한 학생들만 남기고 모두 삭제하세요. 

test_none = stu_data['test preparation course'] == 'none'
stu_data_test_none = stu_data[test_none]
print(stu_data.drop(stu_data_test_none.index))

#   7. 6의 결과로 나온 학생들의 Listening score를 추가하세요   
#   - Hint. Random 함수를 사용해서 학생 수만큼 0~100점 사이의 랜덤한 점수를 추가해서 사용
deleted_stu_data=stu_data.drop(stu_data_test_none.index)
deleted_stu_data.loc[1,'Listening'] = random.randint(0,100)
i = 0
for i in deleted_stu_data.index:
    deleted_stu_data.loc[i,'Listening'] = random.randint(0,100)
print(deleted_stu_data)
#   4번 문제
# print('group C 여자의 평균')
# c = stu_data['race/ethnicity'] == 'group C'
# sex_female = stu_data['gender'] == 'female'
# print(stu_data.loc[c & sex_female,'math score':].mean())
# print()
# print('group C 남자의 평균')
# sex_male = stu_data['gender'] == 'male'
# print(stu_data.loc[c & sex_male,'math score':].mean())


#   3번 문제
# print('A 그룹의 평균')
# a = stu_data['race/ethnicity'] == 'group A'
# print(stu_data.loc[a,'math score':].mean())
# print()

# #   B 그룹의 평균
# print('B 그룹의 평균')
# b = stu_data['race/ethnicity'] == 'group B'
# print(stu_data.loc[b,'math score':].mean())
# print()

# #   C 그룹의 평균
# print('C 그룹의 평균')
# c = stu_data['race/ethnicity'] == 'group C'
# print(stu_data.loc[c,'math score':].mean())
# print()

# #   D 그룹의 평균
# print('D 그룹의 평균')
# d = stu_data['race/ethnicity'] == 'group D'
# print(stu_data.loc[d,'math score':].mean())
# print()

# #   E 그룹의 평균
# print('E 그룹의 평균')
# e = stu_data['race/ethnicity'] == 'group E'
# print(stu_data.loc[e,'math score':].mean())
# print()




# 2번 문제
# print(stu_data.iloc[:,5:].max())  # 최대값
# print()
# print(stu_data.iloc[:,5:].min())  # 최소값
# print()
# print(stu_data.iloc[:,5:].mean())  # 평균값



# 5번 문제
# more80 = stu_data['math score'] > 80
# sex = stu_data['gender'] == 'male'
# male_count=stu_data.loc[more80&sex]
# print(len(male_count.index))

