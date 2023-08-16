# may23-team11
Team member=Ramesh(Ram) & Chan
I've choose the catboost model with hyperparameter tuning
Decided to withdraw customer_status variable as it gives bias answers
AUC is 0.80 
http://13.212.164.69/
http://18.136.200.14/ # this is for CI/CD workflow

## AI300 Capstone Grading

### Feedback from Instructor Min Yan

Good work on the capstone project! It's a pity that you didn't share your research .ipynb in this codebase, so I found it a little challenging to locate your codes for the visualisations and hyperparameter tuning logic.

An area of improvement would be to try directly ingesting your dataset via SQL connection in Python, rather than using SQL in workbench and then import your dataset as .csv (which is similar to what we have done in AI200).

Overall, well done on the capstone! Keep up the good work!

### Total Score: 20 / 20

Data Exploration: 6 / 6 marks
- [x] SQL used to successfully retrieve dataset from remote Heicoders database
- [x] SQL query should retrieve at least one column from each table:
churn_status, account, account_usage, customer and city tables
- [x] At least 2 charts used to visualise columns in dataset (e.g. with matplotlib or plotly)
- [x] Evidence of data preprocessing and/or feature engineering
e.g. column data type conversions, handling missing values, one hot encoding, etc.

Model Selection: 5 / 5 marks
- [x] Experiment with at least 2 model algorithms (e.g. catboost, xgboost, lgbm)
- [x] Evidence of hyperparameter tuning (e.g. GridSearchCV, RandomizedSearchCV, etc)
- [x] Calculate offline AUC of selected model
- [x] Export selected final model to .pkl file using joblib library

Remote GitHub Repository: 4 / 4 marks
- [x] Evidence of multiple commits with meaningful commit messages
- [x] Contains latest code for research & Flask web app _(missing .ipynb)_
- [x] Contains required documentation specified in grading rubric

Flask Web Application: 5 / 5 marks
- [x] Implement Model() class that loads model from .pkl file and generate predictions
- [x] Web app should support functionality of generating binary predictions
- [x] Web app is hosted on a publicly accessible website
# CICD-AI300
