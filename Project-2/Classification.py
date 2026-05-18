import pandas as pd
from sklearn.model_selection import train_test_split # Helps us split data into training and testing data
from sklearn.preprocessing import StandardScaler    # This tool normalizes/scales the data
from sklearn.neighbors import KNeighborsClassifier  # # Import K-Nearest Neighbors classifier
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score # These measure how good the model performed.
from sklearn.preprocessing import LabelEncoder


# Importing the dataset
iris_data = pd.read_csv("C:/Users/hp/PycharmProjects/PythonProject/Artificial Intelligence/Project-2/iris.csv")

# Look at the data set
print("First 5 Rows of Dataset:\n")
print(iris_data.head())

# Separating Input and Output
X = iris_data.drop("species",axis=1)
Y = iris_data["species"]

# To avoid string errors
encoder = LabelEncoder()
Y = encoder.fit_transform(Y)

# Splitting the dataset
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


# Scaling the Data

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creating the AI model

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train,Y_train)

# Now we ask the model to predict
predictions = model.predict(X_test)

#F1 score
f1 = f1_score(Y_test,predictions,average="weighted")


#accuracy score
acc = accuracy_score(Y_test,predictions)


#Confusion matrix
cm = confusion_matrix(Y_test,predictions)


print("\n========== MODEL RESULTS ==========\n")

print(f"Accuracy Score: {acc:.2f}\n")

print("Confusion Matrix:")
print(cm)

print("\nF1 score:")
print(f1)

print("===================================")















