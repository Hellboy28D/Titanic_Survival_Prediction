from utils import *;

titanic_data = pd.read_csv('/train.csv')

print(titanic_data.head())
print(titanic_data.shape)
print(titanic_data.info())
print(titanic_data.isnull().sum())

titanic_data = titanic_data.drop(columns='Cabin', axis=1)

titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)

print(titanic_data['Embarked'].mode())
print(titanic_data['Embarked'].mode()[0])

titanic_data['Embarked'].fillna(titanic_data['Embarked'].mean()[0], inplace=True)
print(titanic_data.isnull().sum())

print(titanic_data.describe())
print(titanic_data['Survived'].value_counts())

# *** Data Visualization ***
sns.set()
sns.countplot('Survived', data=titanic_data)

print(titanic_data['Sex'].value_counts())
sns.countplot('Sex', data=titanic_data)

sns.countplot('Sex',hue='Survived' ,data=titanic_data)
sns.countplot('Pclass',hue='Survived' ,data=titanic_data)