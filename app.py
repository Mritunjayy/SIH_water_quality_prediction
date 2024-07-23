from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load('multioutput_xgboost_model.pkl')

@app.route('/')
def home():
    
    return render_template('index.html')  
@app.route('/feasible',methods=['POST'])
def feasible():
    try:
        input1 = float(request.form['quantity'])
        input2 = float(request.form['quantity'])
        predictions = model.predict([[input1,input2]])
        # HCO3- 30-400
        # SO4-<500
        if(((predictions[:,2]<400) and (predictions[:,2]>30)) and (predictions[:,5]<500)):
            result = ('''since the CO3 content is {} and SO4 content is {} , henece water well construction is feasible,'''.format(predictions[:,2],predictions[:,5]))
        else:
            result =  ('''the CO3 content is {} and SO4 content is {} , hence Not feasible to construct well '''.format(predictions[:,2],predictions[:,5]))
        return render_template('feasible.html', result=result)
    except Exception as e:
        return "error" 
    

@app.route('/predict', methods=['POST'])
def predict():
    try:

        input1 = float(request.form['quantity'])
        input2 = float(request.form['quantity'])

        predictions = model.predict([[input1,input2]])
        if (((predictions[:,0]<8.5) and (predictions[:,0]>6.5)) and (predictions[:,14]<1300) and (predictions[:,1]<1000)):
            result =  ("Your pH level of water is {}  , Electrical conductivity is {} while your TDS content is {} and therefore the water quality is good for drinking".format(predictions[:,0],predictions[:,1],predictions[:,14]))
        else:
            result =  ("pH level is {}  , Electrical conductivity is {} while your TDS content is {}, and hence not safe for drinking".format(predictions[:,0],predictions[:,1],predictions[:,14]))

        return render_template('predict.html', result=result)

    except Exception as e:
        return ('error')
    

if __name__ == '__main__':
    app.run(debug=True) 