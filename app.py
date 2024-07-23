# import streamlit as st
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the saved model
model = joblib.load('multioutput_xgboost_model.pkl')

@app.route('/')
def home():
    # return 'fuck jinja2'
    return render_template('index.html')  # Create an HTML template for your website
@app.route('/feasible',methods=['POST'])
def feasible():
    try:
        input1 = float(request.form['quantity'])
        input2 = float(request.form['quantity'])
        predictions = model.predict([[input1,input2]])
        # HCO3- 30-400
        # SO4-<500
        if(((predictions[:,2]<400) and (predictions[:,2]>30)) and (predictions[:,5]<500)):
            return   '''since the CO3 content is {} and SO4 content is {} , hene
                        water well construction is feasible,'''.format(predictions[:,2],predictions[:,5])
        else:
            return ('''the CO3 content is {} and SO4 content is {} , hence
                     Not feasible to construct well '''.format(predictions[:,2],predictions[:,5]))
    except Exception as e:
        return "error" 
    

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the website's form or API request
        input1 = float(request.form['quantity'])
        input2 = float(request.form['quantity'])
        # print(input1)
        # print(input2)
        # input_data=(input1,input2).toarray()
        # input_data = request.form  # Adjust this based on your website's form structure
        # input_data=[[input1,input2]]

        # Preprocess the input data if needed

        # Make predictions using the loaded model
        predictions = model.predict([[input1,input2]])
        if (((predictions[:,0]<8.5) and (predictions[:,0]>6.5)) and (predictions[:,14]<1300) and (predictions[:,1]<1000)):
            return ("Your pH level of water is {}  , Electrical conductivity is {} while your TDS content is {} and therefore the water quality is good for drinking".format(predictions[:,0],predictions[:,1],predictions[:,14]))
        else:
            return ("pH level is {}  , Electrical conductivity is {} while your TDS content is {}, and hence not safe for drinking".format(predictions[:,0],predictions[:,1],predictions[:,14]))

        # You can process the predictions further if necessary
        # return predictions
        # Return the predictions as JSON
        # return jsonify({'your pH is:-': predictions.tolist()})
    except Exception as e:
        return ('error')
        # return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 