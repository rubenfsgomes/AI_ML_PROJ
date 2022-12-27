import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
from sklearn.svm import SVC

# create the vectorizer object
vectorizer = CountVectorizer()

# read the new error logs from the .txt file
with open('new_error_logs.txt', 'r') as f:
    new_error_logs = f.readlines()


# load the data from the .csv file
df = pd.read_csv('error_logs.csv')

# extract the error logs and solutions from the dataframe
X = df['error_log']
y = df['solution']

# convert the error logs to a matrix of token counts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create a logistic regression model
model = SVC(C=1.0, kernel='rbf')

# train the model on the training data
model.fit(X_train, y_train)

dump(vectorizer, 'vectorizer.joblib')
dump(model, 'model.joblib')

# evaluate the model on the test data
accuracy = model.score(X_test, y_test)
print('Accuracy:', accuracy)

'''
dump(vectorizer, 'vectorizer.joblib')
'''

'''
# load the model and vectorizer objects
vectorizer = load('vectorizer.joblib')
model = load('model.joblib')
'''

# read the new error logs from the .txt file
with open('new_error_logs.txt', 'r') as f:
    new_error_logs = f.readlines()

# use the model to make predictions on the new error logs
predictions = model.predict(vectorizer.transform(new_error_logs))
print('Predictions:', predictions)


# write the predictions to the output file
with open('predictions.txt', 'w') as f:
    for prediction in predictions:
        f.write(prediction + '\n')

