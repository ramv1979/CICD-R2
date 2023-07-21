import pandas as pd

def load_data():
    # Specify the file path
    data = pd.read_csv(r'C:/Users/v-ram/Downloads/may23-team11/data/Merged Data Capstone1.csv')

    return data

# Run the code
if __name__ == "__main__":
    data = load_data()
    print(data)


