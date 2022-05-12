import pickle
import numpy as np
<<<<<<< HEAD
=======

>>>>>>> 01601247a03d8a041a168b9bd8ac6ca4bf7fefa6
def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]
<<<<<<< HEAD
with open('churn-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
    
customer = {
    'customerid': '8879-zkjof',
    'gender': 'male',
=======

with open('churn-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
    

customer = {
    'customerid': '8879-zkjof',
    'gender': 'female',
>>>>>>> 01601247a03d8a041a168b9bd8ac6ca4bf7fefa6
    'seniorcitizen': 0,
    'partner': 'no',
    'dependents': 'no',
    'tenure': 41,
    'phoneservice': 'yes',
    'multiplelines': 'no',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'no',
    'deviceprotection': 'yes',
    'techsupport': 'yes',
    'streamingtv': 'yes',
    'streamingmovies': 'yes',
    'contract': 'one_year',
    'paperlessbilling': 'yes',
    'paymentmethod': 'bank_transfer_(automatic)',
<<<<<<< HEAD
    'monthlycharges': 2079.85,
    'totalcharges': 13320.75,
}
 
prediction = predict_single(customer, dv, model)
=======
    'monthlycharges': 279.85,
    'totalcharges': 1320.75,
}
 
prediction = predict_single(customer, dv, model)

>>>>>>> 01601247a03d8a041a168b9bd8ac6ca4bf7fefa6
print('prediction: %.3f' % prediction)
 
if prediction >= 0.5:
    print('verdict: Churn')
else:
<<<<<<< HEAD
    print('verdict: Not churn')
=======
    print('verdict: Not churn')
>>>>>>> 01601247a03d8a041a168b9bd8ac6ca4bf7fefa6
