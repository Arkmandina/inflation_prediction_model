from sqlalchemy import create_engine
from config import username, password, hostname, port, db
import pandas as pd
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
# Load the model
model = pickle.load(open('./model.pkl','rb'))


engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')

@app.route('/')
def home():
    return render_template("index.html")

# Define route for global inflation json data
@app.route("/api/v1.0/inflation_gdp")
def inflation_data():
    conn = engine.connect()
    query = "SELECT * FROM inflation_gdp"
    df = pd.read_sql(query,conn)
    return df.to_json(orient = 'records')

# Define route for prediction 
@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":

        # get the input data from the user to predict the inflation      
        country_id = request.form['country']
        print (request.form)        
        year = request.form["year"]
        gdp = float(request.form["gdp"])
        interestRate = float(request.form["int"])
        unemployment = float(request.form["unemp"])

        features = pd.DataFrame([[country_id, year, gdp, interestRate, unemployment]], columns = ['country_id', 'year', 'gdp', 'interestRate', 'unemployment'])
        print(features)
        # Make prediction using model loaded from disk as per the data.

        prediction = model.predict(features)[0]

        result = ''
        if prediction == 0:
            result = 'Not Inflated'

        else : 
            result = 'Inflated'
                
        return render_template("results.html", output = result)

if __name__ == "__main__":
    app.run(debug = True)