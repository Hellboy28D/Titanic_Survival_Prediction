# Titanic Survival Prediction using Machine Learning 🚢

Predicting passenger survival on the Titanic using Logistic Regression, Python, and Scikit-learn.

⸻

📖 Overview

The Titanic Survival Prediction project is a beginner-friendly yet comprehensive Machine Learning project that predicts whether a passenger survived the Titanic disaster based on features such as age, gender, passenger class, fare, and embarkation point.

The project demonstrates the complete Machine Learning workflow, including:

* Data Collection
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Data Visualization
* Model Training
* Model Evaluation
* Performance Analysis

The dataset used is the famous Titanic Dataset from Kaggle, which has become one of the most widely used datasets for learning classification algorithms.

⸻

🎯 Objective

The primary objective of this project is to build a binary classification model capable of predicting whether a passenger survived the Titanic disaster.

The project also focuses on understanding how different passenger attributes influence survival probability.

⸻

📂 Project Structure

Titanic_Survival_Prediction
│
├── train.py                 # Model Training
├── preprocess.py            # Data Cleaning & Preprocessing
├── utils.py                 # Utility Functions
├── train.csv                # Titanic Dataset
├── requirements.txt         # Python Dependencies
├── README.md

⸻

📊 Dataset

The dataset contains passenger information collected from the Titanic.

Some important features include:

Feature	Description
PassengerId	Unique Passenger ID
Survived	Target Variable (0 = No, 1 = Yes)
Pclass	Passenger Class
Name	Passenger Name
Sex	Gender
Age	Passenger Age
SibSp	Number of siblings/spouses aboard
Parch	Number of parents/children aboard
Ticket	Ticket Number
Fare	Ticket Fare
Cabin	Cabin Number
Embarked	Port of Embarkation

⸻

⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn

⸻

📚 Python Libraries

numpy
pandas
matplotlib
seaborn
scikit-learn

⸻

🔄 Machine Learning Workflow

1. Import Libraries

The project begins by importing essential libraries for:

* Data manipulation
* Data visualization
* Model training
* Performance evaluation

⸻

2. Load Dataset

pd.read_csv("train.csv")

The Titanic dataset is loaded into a Pandas DataFrame.

⸻

3. Exploratory Data Analysis

The project performs several analyses including:

* Dataset shape
* Dataset information
* Missing values
* Statistical summary
* Survival distribution
* Gender distribution
* Passenger class distribution

⸻

4. Data Cleaning

Several preprocessing techniques are applied.

Removing Cabin Column

The Cabin column contains too many missing values.

drop("Cabin")

⸻

Filling Missing Age Values

Missing ages are replaced using the mean age.

fillna(mean)

⸻

Filling Embarked Values

Missing embarkation values are replaced with the most frequent category.

⸻

5. Feature Encoding

Machine Learning models require numerical input.

Categorical variables are encoded:

Feature	Encoding
Male	0
Female	1
Southampton	0
Cherbourg	1
Queenstown	2

⸻

6. Feature Selection

Input Features:

Passenger Class
Sex
Age
Siblings/Spouse
Parents/Children
Fare
Embarked

Target Feature:

Survived

⸻

7. Train-Test Split

The dataset is divided into:

* 80% Training Data
* 20% Testing Data

train_test_split()

⸻

8. Model Training

The project uses Logistic Regression.

model = LogisticRegression()
model.fit(X_train, Y_train)

Logistic Regression is an excellent baseline algorithm for binary classification problems because it is simple, interpretable, and computationally efficient.

⸻

9. Model Evaluation

Model performance is evaluated using:

* Training Accuracy
* Testing Accuracy

accuracy_score()

⸻

📈 Data Visualizations

The following visualizations are created:

* Survival Count Plot
* Gender Distribution
* Survival by Gender
* Survival by Passenger Class

These visualizations help understand important patterns in the dataset.

⸻

📊 Example Output

Dataset Shape
(891, 12)
Training Accuracy
82%
Testing Accuracy
80%

(Results may vary depending on preprocessing and random state.)

⸻

🧠 Machine Learning Concepts Covered

* Binary Classification
* Logistic Regression
* Data Cleaning
* Missing Value Handling
* Feature Encoding
* Data Visualization
* Exploratory Data Analysis
* Train-Test Split
* Model Evaluation
* Accuracy Score

⸻

🚀 Installation

Clone the repository:

git clone https://github.com/Hellboy28D/Titanic_Survival_Prediction.git

Move into the project folder:

cd Titanic_Survival_Prediction

Install the dependencies:

pip install -r requirements.txt

⸻

▶️ Running the Project

Execute:

python train.py

The program will:

* Load the dataset
* Clean the data
* Visualize important features
* Train the Logistic Regression model
* Predict passenger survival
* Display training and testing accuracy

⸻

📌 Future Improvements

Some possible enhancements include:

* Random Forest Classifier
* XGBoost Classifier
* Support Vector Machine (SVM)
* Gradient Boosting
* Hyperparameter Tuning
* Cross Validation
* Feature Scaling
* Feature Engineering
* Model Serialization using Pickle or Joblib
* Interactive Web Application with Flask or Streamlit
* Docker support for deployment
* CI/CD pipeline using GitHub Actions

⸻

📈 Learning Outcomes

By completing this project, you will gain hands-on experience with:

* Real-world data preprocessing
* Handling missing values
* Exploratory Data Analysis
* Data visualization using Seaborn
* Building classification models
* Evaluating model performance
* Working with Scikit-learn pipelines
* End-to-end Machine Learning workflows

⸻

🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

⸻

⭐ If You Like This Project

If you found this project helpful:

* ⭐ Star this repository
* 🍴 Fork the project
* 🐛 Report issues
* 💡 Suggest new features
* 📢 Share it with others

⸻

📜 License

This project is open-source and available under the MIT License.

⸻

👨‍💻 Author

Divakar Daya

* GitHub: https://github.com/Hellboy28D
* Passionate about Machine Learning, Data Science, Artificial Intelligence, Rust Systems Programming, Backend Development, and Open Source.

⸻

“Machine Learning is not just about making predictions—it’s about discovering patterns hidden within data and transforming them into meaningful insights.”
