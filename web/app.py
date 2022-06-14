from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib


app = Flask(__name__)

model = joblib.load('model.pkl')
#transformer = joblib.load('trans.joblib')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    int_features = [x for x in request.form.values()]
    
    features = [np.array(int_features)]
    
    columns = ['NAME_CONTRACT_TYPE', 'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY','CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY','AMT_GOODS_PRICE', 'NAME_TYPE_SUITE', 'NAME_INCOME_TYPE','NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE','REGION_POPULATION_RELATIVE', 'DAYS_BIRTH', 'DAYS_EMPLOYED','DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'FLAG_MOBIL', 'FLAG_EMP_PHONE','FLAG_WORK_PHONE', 'FLAG_CONT_MOBILE', 'FLAG_PHONE', 'FLAG_EMAIL','OCCUPATION_TYPE', 'CNT_FAM_MEMBERS', 'REGION_RATING_CLIENT','REGION_RATING_CLIENT_W_CITY', 'WEEKDAY_APPR_PROCESS_START','HOUR_APPR_PROCESS_START', 'REG_REGION_NOT_LIVE_REGION','REG_REGION_NOT_WORK_REGION','LIVE_REGION_NOT_WORK_REGION','REG_CITY_NOT_LIVE_CITY', 'REG_CITY_NOT_WORK_CITY','LIVE_CITY_NOT_WORK_CITY', 'ORGANIZATION_TYPE','OBS_30_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE','OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE','DAYS_LAST_PHONE_CHANGE']

    #df = pd.DataFrame(data=features,columns=columns)

    num_col = ['CNT_CHILDREN',
                'AMT_INCOME_TOTAL',
                'AMT_CREDIT',
                'AMT_ANNUITY',
                'AMT_GOODS_PRICE',
                'REGION_POPULATION_RELATIVE',
                'DAYS_BIRTH',
                'DAYS_EMPLOYED',
                'DAYS_REGISTRATION',
                'DAYS_ID_PUBLISH',
                'CNT_FAM_MEMBERS',
                'HOUR_APPR_PROCESS_START',
                'OBS_30_CNT_SOCIAL_CIRCLE',
                'DEF_30_CNT_SOCIAL_CIRCLE',
                'OBS_60_CNT_SOCIAL_CIRCLE',
                'DEF_60_CNT_SOCIAL_CIRCLE',
                'DAYS_LAST_PHONE_CHANGE']

    #for i in num_col:
    #    df[i] = df[i].astype('float64')


    

    # transformer = make_column_transformer(
    #     (MinMaxScaler(), selector(dtype_exclude=object)),
    #     (OneHotEncoder(handle_unknown='ignore'), selector(dtype_include=object)))
    #transformer.fit(df)
    #df = transformer.transform(df)
    #print(df.shape)
    prediction = model.predict(features)

    return render_template('index.html', df = prediction)

if __name__ == "__main__":
    app.run(debug=True)
