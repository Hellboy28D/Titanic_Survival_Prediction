from utils import *;
from preprocess import *;

# *** Encoding the Categorical Columns ***
print(titanic_data['Sex'].value_counts())

print(titanic_data['Embarked'].value_counts())

# Converting the categorical Columns

titanic_data.replace({'Sex':{'male': 0, 'female':1}, 'Embarked': {'S':0,'C':1,'Q':2}}, Inplace = True)
print(titanic_data.head())

X = titanic_data.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Survived'], axis =1)
Y = titanic_data['Survived']

#data into Splitting the  Training & Testing data

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state =2)
