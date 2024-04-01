import pandas as pd

df = pd.DataFrame({'name' : ['Minsoo','Minju','Yeomin','Hyeri','Junghun','Sunny','Bummee','Luna'],
                   'old'  : [33,25,19,25,32,36,23,36],
                   'sex'  : ['M','W','W','W','M','W','M','W'],
                   'score1': [91,50,69,98,72,85,43,61], 
                   'score2': [65,77,56,82,79,91,71,63],
                   'time' : [30,95,64,88,34,69,15,25],
                   })
over_20 = df['old'] > 20
sexm = df['sex'] == 'M'
print(over_20[])