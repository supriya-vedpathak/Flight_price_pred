import  pandas as pd
import numpy as np
from datetime import date
import datetime
import pickle
import json

class Flight_Class():
    def __init__(self , airline,departure,stops,arrival,
                    Class,days, source_city , destination_city ):
        self.airline=airline
        self.departure=departure
        self.stops=stops
        self.arrival=arrival              
        self.Class=Class
       
        self.days=days
        self.source_city =source_city
        self.destination_city=destination_city
        
        with open ('linreg.pkl','rb') as f:
            self.model = pickle.load(f)

        with open ('column_data.json','r') as f:
            self.column_data = json.load(f)

    def predict_price(self):

        tsry = np.zeros(self.model.n_features_in_)

        tsry[0] = self.column_data['airline'][self.airline]
        tsry[1] = self.column_data['departure_time'][self.departure]
        tsry[2] = self.column_data['stops'][self.stops]
        tsry[3] = self.column_data['arrival_time'][self.arrival]
        tsry[4] = self.column_data['Class'][self.Class]
        tsry[5] = self.days
        
        s_index = self.column_data["Column_Names"].index('source_city_'+ self.source_city)
        tsry[s_index]= 1
        d_index = self.column_data["Column_Names"].index('destination_city_'+ self.destination_city)
        tsry[d_index]= 1

        FP = self.model.predict([tsry])
        return FP