from data_loader import load_data

# Call the load_data function
data = load_data()

print(data)

# Convert Yes or No to binary values

data['churn_label'] = data['churn_label'].map({'Yes': 1, 'No': 0})

# Calculate the median of 'churn_label'
median_churn_label = data['churn_label'].median()

# Impute missing values with the median
data['churn_label'] = data['churn_label'].fillna(median_churn_label)

# Convert 'churn_label' back to integer data type
data['churn_label'] = data['churn_label'].astype(int)

# Print the modified data
print(data['churn_label'])

# Unique values after imputation
unique_values = data['churn_label'].unique()
print(unique_values)



# Get the initial length of the DataFrame
initial_length = len(data)

# Drop duplicate rows based on 'account_id'
data.drop_duplicates(subset='account_id', keep='first', inplace=True)

# Get the length of the DataFrame after dropping duplicates
final_length = len(data)

# Compare the lengths
if initial_length == final_length:
    print("No duplicate rows found.")
else:
    print("Duplicate rows have been dropped.")

print(data)


# Check missing data for all variables
missing_data = data.isnull().sum()
print(missing_data)


data.describe()
data.info()

# Print columns before dropping
print("Columns before dropping:")
print(data.columns)

# Drop specific columns
columns_to_drop = ['account_id.1', 'customer_id.1', 'customer_id.2', 'zip_code.1']
data = data.drop(columns_to_drop, axis=1)

# Print columns after dropping
print("Columns after dropping:")
print(data.columns)

data.info()
# Check missing data for all variables
missing_data = data.isnull().sum()
print(missing_data)


#Checking the mean of Churn_Category
import matplotlib.pyplot as plt
churn_proportions = data.groupby('churn_category')['churn_label'].mean()
churn_proportions.plot(kind='bar')
plt.ylabel('Proportion of Churn')
plt.show()

#Checking the mean of Churn_Reason
import matplotlib.pyplot as plt
churn_proportions = data.groupby('churn_reason')['churn_label'].mean()
churn_proportions.plot(kind='bar')
plt.ylabel('Proportion of Churn')
plt.show()



# Check missing data for all variables
missing_data = data.isnull().sum()
print(missing_data)


# Drop the churn_category column
data = data.drop('churn_category', axis=1)
print(data.columns)
missing_data = data.isnull().sum()
print(missing_data)



# Check the data types of variables in the DataFrame
print(data.dtypes)


# Impute the missing values in the 'churn_reason' column with the most frequent value
from sklearn.preprocessing import LabelEncoder

# Impute the missing values in the 'churn_reason' column with the most frequent value
most_frequent_value = data['churn_reason'].mode().iloc[0]
data['churn_reason'] = data['churn_reason'].fillna(most_frequent_value)

# Select only the object variables
object_vars = data.select_dtypes(include='object')

# Print the object variables
print(object_vars)


# Create an instance of LabelEncoder
label_encoder = LabelEncoder()

# Encode the values of object_vars using LabelEncoder
encoded_object_vars = object_vars.apply(lambda x: label_encoder.fit_transform(x.astype(str)))

# Print the encoded object variables
print(encoded_object_vars)

# Check for missing data
missing_data = data.isnull().sum()
print(missing_data)



# Select numeric variables for correlation analysis
numeric_vars = ['tenure_months', 'num_referrals', 'avg_long_distance_fee_monthly', 'total_long_distance_fee', 'avg_gb_download_monthly', 'total_monthly_fee', 'total_charges_quarter', 'total_refunds', 'age', 'num_dependents', 'area_id', 'zip_code', 'latitude', 'longitude', 'population']

# Calculate correlation matrix
correlation_matrix = data[numeric_vars].corr()

# Display the correlation matrix
print(correlation_matrix)



# String to integar (internet_type)
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data['internet_type'] = label_encoder.fit_transform(data['internet_type'])
print(data['internet_type'].unique())



# String to integar (All below variables:)
binary_vars = ['has_internet_service', 'has_unlimited_data', 'has_phone_service', 'has_multiple_lines',
               'has_premium_tech_support', 'has_online_security', 'has_online_backup', 'has_device_protection']
for var in binary_vars:
    data[var] = data[var].replace({'No': 0, 'Yes': 1})
for var in binary_vars:
    print(data[var].unique())
binary_vars = ['has_internet_service', 'has_unlimited_data', 'has_phone_service', 'has_multiple_lines',
               'has_premium_tech_support', 'has_online_security', 'has_online_backup', 'has_device_protection']
for var in binary_vars:
    data[var] = data[var].replace({'No': 0, 'Yes': 1})
for var in binary_vars:
    print(data[var].dtype)

# String to integar (All below variables:)
contract_type_mapping = {'One Year': 1, 'Two Year': 2, 'Month-to-Month': 3}
paperless_billing_mapping = {'No': 0, 'Yes': 1}
payment_method_mapping = {'Credit Card': 1, 'Bank Withdrawal': 2, 'Mailed Check': 3}
data['contract_type'] = data['contract_type'].map(contract_type_mapping)
data['paperless_billing'] = data['paperless_billing'].map(paperless_billing_mapping)
data['payment_method'] = data['payment_method'].map(payment_method_mapping)

print(data['contract_type'].unique())
print(data['paperless_billing'].unique())
print(data['payment_method'].unique())


# String to integar (All below variables:)
stream_mapping = {'No': 0, 'Yes': 1}
data['stream_tv'] = data['stream_tv'].map(stream_mapping)
data['stream_movie'] = data['stream_movie'].map(stream_mapping)
data['stream_music'] = data['stream_music'].map(stream_mapping)

print(data['stream_tv'].unique())
print(data['stream_movie'].unique())
print(data['stream_music'].unique())


# String to integar (All below variables:)
customer_status_mapping = {'Stayed': 0, 'Churned': 1, 'Joined': 2}
gender_mapping = {'Male': 0, 'Female': 1}
yes_no_mapping = {'No': 0, 'Yes': 1}

data['customer_status'] = data['customer_status'].map(customer_status_mapping)
data['gender'] = data['gender'].map(gender_mapping)
data['senior_citizen'] = data['senior_citizen'].map(yes_no_mapping)
data['married'] = data['married'].map(yes_no_mapping)

print(data['customer_status'].unique())
print(data['gender'].unique())
print(data['senior_citizen'].unique())
print(data['married'].unique())


# Check the data types of all columns
print(data.dtypes)

# Check for missing data
missing_data = data.isnull().sum()
# Print the missing data
print(missing_data)



# Merged internet_variable
data['internet_merged_variable'] = data['internet_type'] + data['has_unlimited_data'] + data['has_phone_service'] 
+ data['has_multiple_lines'] + data['has_premium_tech_support'] + data['has_online_security'] + data['has_online_backup'] + data['has_device_protection']

#Drop after merging
columns_to_drop = ['internet_type', 'has_unlimited_data', 'has_phone_service', 'has_multiple_lines', 'has_premium_tech_support', 'has_online_security', 'has_online_backup', 'has_device_protection']
data = data.drop(columns_to_drop, axis=1)

# Check the unique values in 'churn_label'
print(data['churn_label'].unique())


# Create a new column 'streaming_services'
data['streaming_services'] = data['stream_tv'] + data['stream_movie'] + data['stream_music']

# Drop the individual streaming columns
data = data.drop(['stream_tv', 'stream_movie', 'stream_music'], axis=1)


from sklearn.preprocessing import LabelEncoder

# Create an instance of LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'city_name' variable
data['city_name_encoded'] = label_encoder.fit_transform(data['city_name'])

# Print the encoded values
print(data['city_name_encoded'])

data = data.drop(['city_name'], axis=1)

