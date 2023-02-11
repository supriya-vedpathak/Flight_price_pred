from flask import Flask, render_template, request
from utils import Flight_Class
from datetime import datetime as dt
import numpy as np
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_flight_price', methods = ['GET', 'POST'])
def get_price():
    data = request.form.get

    airline = data('airline')
    departure = data('departure_time')
    stops = data('stops')
    arrival = data('arrival_time')
    Class = data ('Class')
    
    # (dt.strptime(data('days_left'), "%d-%m-%Y")
    days = (dt.strptime(data('days_left'), "%Y-%m-%d") - dt.now()).days
    source_city = data('source_city')
    destination_city= data('destination_city')

    f_obj = Flight_Class(airline,departure,stops,arrival,
                    Class,days,source_city,destination_city)
    price = f_obj.predict_price()

    return render_template('result.html' , Price  = np.around(price,2))

if __name__ == ("__main__"):
    app.run(host= '0.0.0.0', port = 5003 , debug = False )