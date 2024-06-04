
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from tensorflow.keras.models import load_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def get_model_predictions(x_train, y_train, X, model_name='SVM', model_object=None):
    replace_encoding = lambda x: 'Succesfully reached Destination' if x>0.5 else 'Failed to reach'
    if model_name == 'SVM':
        model = SVC(probability=True)
        model.fit(x_train,y_train)
        y = model.predict_proba(X.reshape(1,-1))
        outcome = y[0][1]
        return outcome, replace_encoding(outcome)
    elif model_name == 'logreg':
        model = LogisticRegression()
        model.fit(x_train,y_train)
        y = model.predict_proba(X.reshape(1,-1))
        outcome = y[0][1]
        return outcome, replace_encoding(outcome)
    elif model_name == 'randomforest':
        model = RandomForestClassifier()
        model.fit(x_train,y_train)
        y = model.predict_proba(X.reshape(1,-1))
        outcome = y[0][1]
        return outcome, replace_encoding(outcome)
    elif model_name == 'xgboost':
        model = XGBClassifier()
        model.fit(x_train,y_train)
        y = model.predict_proba(X.reshape(1,-1))
        outcome = y[0][1]
        return outcome, replace_encoding(outcome)
    elif model_name == 'dnn':
        model = model = load_model('keras_model.h5')
        y = model.predict(X.reshape(1,-1))
        outcome = y[0][0]
        return outcome, replace_encoding(outcome)

def encode_input(home_planet, cyro, dest, age,travel_company, vip, room_service, food_court, cols, p_s):
    context = {
        'HomePlanet' : {'Europa': 0, 'Earth': 1, 'Mars': 2},
        'CryoSleep' : {False: 0, True: 1},
        'Destination' : {'TRAPPIST-1e': 0, 'PSO J318.5-22': 1, '55 Cancri e': 2},
        'Travel_company' : {'Tulsa Inc': 0, 'Blue Horizon': 1},
        'P_S' : {'P': 0, 'S': 1},
        'Cols' : {'B': 0, 'F': 1, 'A': 2, 'G': 3, 'E': 4, 'D': 5, 'C': 6, 'T': 7},
        'VIP' : {False: 0, True: 1},
    }
    home_planet_en = context['HomePlanet'][home_planet]
    cyro_en = context['CryoSleep'][cyro]
    dest_en = context['Destination'][dest]
    travel_company_en = context['Travel_company'][travel_company]
    p_s_en = context['P_S'][p_s]
    cols_en = context['Cols'][cols]
    vip_en = context['VIP'][vip]
    
    inp = np.array([home_planet_en, cyro_en, dest_en, age,travel_company_en, vip_en, room_service, food_court, cols_en, p_s_en])
    return inp

def get_split():
    df = pd.read_csv('preprocessed.csv')
    y = df['Travel Outcome']
    X = df.drop(['Travel Outcome','Unnamed: 0'],axis=1)
    print(X.columns)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
    sc = StandardScaler().fit(X_train)
    X_train_std = sc.transform(X_train)
    return X_train_std,y_train