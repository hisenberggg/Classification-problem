import json
from sqlite3 import paramstyle
from flask import Flask, request, jsonify
from utils import get_model_predictions, encode_input, get_split

app = Flask(__name__)

# For testing in postman: 
# params 
# home_planet  -> Mars / Earth / Europa
# cyro  -> True / False
# dest  -> TRAPPIST-1e / PSO J318.5-22 / 55 Cancri e
# age  -> <integer>
# travel_company  -> Blue Horizon / Tulsa Inc
# vip  -> True / False
# room_service  -> float
# food_court  -> float 
# cols  -> A / B / C / D / E / F / G / T
# p_s  -> P / S 
# model_name  -> logreg / SVM / randomforest / xgboost / dnn 

@app.route('/getpred/', methods=['GET','POST'])
def query_records():
    if request.method == 'GET':
        data = request.args
        home_planet = data['home_planet']
        cyro = (data['cyro'] == 'True')
        dest = data['dest']
        age = int(data['age'])
        travel_company = data['travel_company']
        vip = (data['vip'] == 'True')
        room_service = float(data['room_service'])
        food_court = float(data['food_court'])
        cols = data['cols']
        p_s = data['p_s']
        model_name = data['model_name']
        print(p_s,cols,food_court,room_service,vip,travel_company,age,dest,cyro,home_planet)

        x_encoded = encode_input(home_planet=home_planet, cyro=cyro, dest=dest, age=age, travel_company=travel_company, vip=vip, room_service=room_service, food_court=food_court, cols=cols, p_s=p_s)
        X_train_std,y_train = get_split()
        print( X_train_std.shape,y_train.shape)
        preds = get_model_predictions(X_train_std, y_train, x_encoded, model_name=model_name)
        context = {
            'prob' : str(preds[0]),
            'outcome' : preds[1]
        }
        print(context)
        return jsonify(context)

app.run(debug=True)