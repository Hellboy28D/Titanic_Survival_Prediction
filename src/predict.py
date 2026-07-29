from utils import *;
from preprocess import *;
from train import *;

model = LogisticRegression()
model.fit(X_train, Y_train)

# Accuracy Score

X_train_prediction = model.predict(X_train)
print(X_train_prediction)

training_data_accuracy = accuracy_score(Y_train,X_train_prediction)
print('Accuracy score of training data:', training_data_accuracy)

X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(Y_test,X_test_prediction)
print('Accuracy score of testing data:', testing_data_accuracy)