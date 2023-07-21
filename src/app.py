
from flask import Flask, render_template, request
from model import Model

app = Flask(__name__)

# Define the mappings or dictionaries
churn_label_mapping = {0: 'No', 1: 'Yes'}

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        # Get the input values from the form
        #customer_status = request.form['customer_status']
        contract_type = request.form['contract_type']
        has_internet_service = request.form['has_internet_service']
        payment_method = request.form['payment_method']
        total_monthly_fee = request.form['total_monthly_fee']
        senior_citizen = request.form['senior_citizen']
        age = request.form['age']
        

        # Create the input dictionary
        input_features = {
            #'customer_status': customer_status,
            'contract_type': contract_type,
            'has_internet_service': has_internet_service,
            'payment_method': payment_method,
            'paperless_billing': paperless_billing,
            'total_monthly_fee': total_monthly_fee,
            'senior_citizen': senior_citizen,
            'age': age,
            
        }

        # Create an instance of the model
        model = Model()

        # Get the prediction
        prediction = model.predict(list(input_features.values()))

        # Map the churn label prediction to 'Yes' or 'No'
        churn_label = churn_label_mapping[prediction]

        # Return the prediction as a response
        return render_template('result.html', prediction=churn_label)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)