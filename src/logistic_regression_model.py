
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import pandas as pd
from data_preprocessor import data


# Select the features you want to use to predict the churn_label
X = data[['customer_status', 'contract_type', 'has_internet_service', 'payment_method', 'paperless_billing', 'total_monthly_fee', 'senior_citizen', 'age']]
y = data['churn_label']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a logistic regression model
model = LogisticRegression(solver='liblinear', random_state=42)

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict probabilities for the test set
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Compute the AUC score
auc_score = roc_auc_score(y_test, y_pred_proba)
print('AUC:', auc_score)

#F1 Score 
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear', random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
average_f1_score = scores.mean()
print('Average F1 score:', average_f1_score)

