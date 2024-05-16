from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
# 4개의 특징 이름을 출력한다. 
print(iris.feature_names)
# 정수는 꽃의 종류를 나타낸다.: 0 = setosa, 1=versicolor, 2=virginica
print(iris.target)

from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

# (80:20)으로 분할한다. 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)
#random_state 학습순서, 동일한 학습에선 같은 숫자 사용해야됨.(0,1,2,3,4 상관없이 동일하기만 하면됨)

print(X_train.shape)
print(X_test.shape)


from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
scores = metrics.accuracy_score(y_test, y_pred)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

#0 = setosa, 1=versicolor, 2=virginica
classes = {0:'setosa',1:'versicolor',2:'virginica'}

# 아직 보지 못한 새로운 데이터를 제시해보자. 
x_new = [[3,4,5,2],
         [5,4,2,2]]
y_predict = knn.predict(x_new)

print(classes[y_predict[0]])
print(classes[y_predict[1]])
