
from data_preprocessor import data
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score
from sklearn.model_selection import GridSearchCV
import joblib

# Select the features you want to use to predict the churn_label
X = data[['contract_type', 'has_internet_service', 'payment_method', 'paperless_billing', 'total_monthly_fee', 'senior_citizen', 'age']]
y = data['churn_label']

# Convert non-integer/nan values to strings
X = X.astype(str)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)

# Define the categorical feature indices
cat_features = [0, 3]

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'learning_rate': [0.1, 0.01, 0.001],
    'depth': [4, 6, 8],
    'iterations': [100, 200, 300],
    # Add more hyperparameters to tune if desired
}

# Create a CatBoostClassifier instance
model = CatBoostClassifier(
    cat_features=cat_features,
    eval_metric='F1',
    random_seed=5,
)

# Perform hyperparameter tuning using GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='f1', cv=3)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters and evaluate the model on the test set
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

test_pred = best_model.predict(X_test)
f1 = f1_score(y_test, test_pred)
auc = roc_auc_score(y_test, test_pred)

print(f'Best Hyperparameters: {best_params}')
print(f'F1 Score: {f1:.4f}')
print(f'AUC Score: {auc:.4f}')

# Save the best model
joblib.dump(best_model, 'model/catboost_model.pkl')