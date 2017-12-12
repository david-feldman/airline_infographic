#all imports here
from __future__ import division
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import patsy
import sklearn.linear_model as linear
import random
from numpy import random as np_random
from geopy.geocoders import Nominatim
sns.set(style="darkgrid")
pd.options.display.max_columns = 20
#import data sets from csv files

airports = pd.read_csv( "airports.csv", sep=",", names =['ID','Name','City','Country','IATA','ICAO','Lat','Long','Alt','TZ','DST','Tzjunk','Type','Source'])
airports = airports[airports['Country'] == 'United States']
flights = pd.read_csv("flight_edges.csv", sep = "\t", names=['Origin', 'Destination', 'Origin_City','Destination_City','Passengers','Seats','Flights', 'Distance','Date','Origin_Pop','Destination_Pop'])
flights = flights.drop('Origin_Pop', 1)
flights = flights.drop('Destination_Pop', 1)
#flights = flights.drop('Distance', 1)
flights = flights.drop('Passengers', 1)
flights = flights.drop('Seats', 1)
airports = airports.drop('ICAO',1)
airports = airports.drop('Tzjunk',1)
airports = airports.drop('Source',1)
airports = airports.drop('TZ',1)
airports = airports.drop('DST',1)


def get_state (row):
    return row['Destination_City'].split(', ')[1]
def get_year (row):
    return int(str(row['Date'])[0:4])
    
def get_month (row):
    return int(str(row['Date'])[4:6])   
    
   

flights['End_State'] = flights.apply (lambda row: get_state (row),axis=1)
flights['Year'] = flights.apply (lambda row: get_year (row),axis=1)
flights['Month'] = flights.apply (lambda row: get_month (row),axis=1)

flights = flights.drop('Date', 1)
flights = flights.drop('Origin_City', 1)
flights = flights.drop('Destination_City', 1)
print flights.head(10)
flights['Origin'] = flights['Origin'].astype('category')
flights['Destination'] = flights['Destination'].astype('category')
flights['Distance'] = flights['Distance'].astype('int')
flights['End_State'] = flights['End_State'].astype('category')
flights['Year'] = flights['Year'].astype('category')
flights['Month'] = flights['Month'].astype('category')
flights['Distance'] = flights['Distance'] * flights['Flights']


sunbelt = ['AL','AZ','FL','GA','NM','SC','TX','AR','NV','NC','OK']
def sun_belt (row):
    if row['End_State'] in sunbelt:
        return 1
    else: 
        return 0
        
flights['Sun_belt'] = flights.apply (lambda row: sun_belt (row),axis=1)
flights.to_pickle("good_flights.pkl")

