import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load the dataset of property sales
data = pd.read_csv('property_sales.csv')

# define the input features and target variable
X = data[['location', 'size', 'age']]
y = data['price']

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create a linear regression model
model = LinearRegression()

# train the model on the training data
model.fit(X_train, y_train)

# evaluate the model on the testing data
score = model.score(X_test, y_test)
print(f"Model R^2 score: {score:.2f}")

# make a prediction for a new property
new_property = [['downtown', 1000, 10]]
prediction = model.predict(new_property)
print(f"Predicted sale price: {prediction[0]:.2f}")
