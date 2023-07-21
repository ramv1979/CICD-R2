import joblib
class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)



# # Add in this code chunk temporarily (delete it after this run)
# beneficiary_example = {
#     "customer_status": 1,
#     "contract_type": 2,
#     "has_internet_service": 1,
#     "payment_method": 1,
#     "paperless_billing": 1,
#     "total_monthly_fee": 50.0,
#     "senior_citizen": 0,
#     "age": 45,
#     "streaming_services": 1,
#     "population": 10000,
#     "avg_gb_download_monthly": 2.0,
#     "city_name_encoded": 1,
#     "internet_merged_variable": 1,
#     "longitude": 30.5,
#     "gender": 0,
#     "avg_long_distance_fee_monthly": 20.0
# }

# model_inputs = list(beneficiary_example.values())

# print(model_inputs)                  
# print(Model().predict(model_inputs)) 

