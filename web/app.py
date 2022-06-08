from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    int_features = [x for x in request.form.values()]
    print(int_features)
    features = [np.array(int_features)]
    # from sklearn.compose import make_column_transformer
    # from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
    # from sklearn.compose import make_column_selector as selector
    # transformer = make_column_transformer(
    #     (MinMaxScaler(), selector(dtype_exclude=object)),
    #     (OneHotEncoder(handle_unknown='ignore'), selector(dtype_include=object)))
    # features = transformer.transform(features)
    prediction = model.predict(features)

    return render_template('index.html', predicted = prediction)

if __name__ == "__main__":
    app.run(debug=True)
