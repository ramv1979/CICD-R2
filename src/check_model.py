import os

# Define the path to the pickle file
pickle_path = 'src/model/catboost_model.pkl'

# Check if the pickle file exists
if os.path.exists(pickle_path):
    print("Model pickle file exists.")
else:
    print("Model pickle file does not exist.")
