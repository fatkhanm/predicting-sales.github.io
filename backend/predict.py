from flask import Flask,request
import joblib
from flask_cors import CORS
import pandas as pd
loaded_model = joblib.load('best_model.pkl')

#create server
app = Flask(__name__)
CORS(app)

def predict(val):
    loaded_model = joblib.load('best_model.pkl')
    fat_content ={
        'low fat' : [0,1,0,0,0],
        'reguler' :[0,0,1,0,0]
    }
    item_type = {
        'baking goods' : [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'breads':[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'breakfast':[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'canned':[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        'dairy':[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        'frozen foods':[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        'fruits and vegetables':[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        'hard drinks':[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        'health and hygiene':[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        'household':[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        'meat':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        'others':[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        'seafood':[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        'snack foods':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        'soft drinks':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        'strachy foods':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]    
    }
    outlet_size = {
        'high':[1,0,0,0],
        'medium':[0,1,0,0],
        'small':[0,0,1,0],
        'unknown':[0,0,0,1]
    }
    outlet_location = {
        'tier 1':[1,0,0],
        'tier 2':[0,1,0],
        'tier 3':[0,0,1]
    }
    outlet_type = {
        'grocery store':[1,0,0,0],
        'supermarket type 1':[0,1,0,0],
        'supermarket type 2':[0,0,1,0],
        'supermarket type 3':[0,0,0,1]
    }
    dp=[]
    dp.append(int(val.get('item_weight')))
    dp.append(int(val.get('item_visibility')))
    dp.append(int(val.get('item_mrp')))
    dp+=fat_content.get(val.get('fat_content'))
    dp+=item_type.get(val.get('item_type'))
    dp+= outlet_size.get(val.get('outlet_size'))
    dp+=outlet_location.get(val.get('outlet_location'))
    dp+= outlet_type.get(val.get('outlet_store'))
    df_p = pd.DataFrame([dp])
    return loaded_model.predict(df_p[:1])

@app.route('/predict',methods = ['POST'])
def postPredict():
    reqData = request.get_json()
    val = reqData['val']
    return str(predict(val)[0])

@app.route('/getDropDown',methods = ["GET"])
def getDropDown():
    return {
        'fat_content':['low fat','reguler'],
        'item_type':['baking goods','breads','breakfast','canned','dairy','frozen foods','fruits and vegetables','hard drinks','health and hygiene','household','meat','others','seafood','snack foods','soft drinks','strachy foods'],
        'outlet_size':['high','medium','small','unknown'],
        'outlet_location':['tier 1','tier 2','tier 3'],
        'outlet_type':['grocery store','supermarket type 1','supermarket type 2','supermarket type 3']
    }



    

#running server
# if __name__ == '__main__':
#        app.run()