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

flights = pd.read_pickle("good_flights.pkl" )

print flights.info()
print flights.head(40)

years = np.sort(flights['Year'].unique())
o = (flights['End_State'].unique())

flight_sums = [0]* 20
distance_sums = [0]* 20
avg_distance = [0]*20
sunbelt_sums = [0] *20
total_to_sun = [0] *20
month_1 = [0] * 20
month_2 = [0] * 20
month_3 = [0] * 20
month_4 = [0] * 20
month_5 = [0] * 20
month_6 = [0] * 20
month_7 = [0] * 20
month_8 = [0] * 20
month_9 = [0] * 20
month_10 = [0] * 20
month_11 = [0] * 20
month_12 = [0] * 20
i = 0
for yr in years:
    flight_sums[i] = flights[flights['Year'] == yr]['Flights'].sum()
    distance_sums[i] = flights[flights['Year'] == yr]['Distance'].sum()
    avg_distance[i] = distance_sums[i]/flight_sums[i]
    sunbelt_sums[i] = flights[flights['Year'] == yr]['Sun_belt'].sum()
    total_to_sun[i] = flight_sums[i] / sunbelt_sums[i]
    month_1[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 1)]['Flights'].sum() / flight_sums[i]
    month_2[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 2)]['Flights'].sum() / flight_sums[i]
    month_3[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 3)]['Flights'].sum() / flight_sums[i]
    month_4[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 4)]['Flights'].sum() / flight_sums[i]
    month_5[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 5)]['Flights'].sum() / flight_sums[i]
    month_6[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 6)]['Flights'].sum() / flight_sums[i]
    month_7[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 7)]['Flights'].sum() / flight_sums[i]
    month_8[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 8)]['Flights'].sum() / flight_sums[i]
    month_9[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 9)]['Flights'].sum() / flight_sums[i]
    month_10[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 10)]['Flights'].sum() / flight_sums[i]
    month_11[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 11)]['Flights'].sum() / flight_sums[i]
    month_12[i] = flights[(flights['Year'] == yr) & (flights['Month'] == 12)]['Flights'].sum() / flight_sums[i]
    i = i + 1
    

    
list1 = [('Year', years),('Flights',flight_sums),('Distance', distance_sums),('Avg_distance',avg_distance)]
list2 = [('Year', years),('Sunbelt_Sum',sunbelt_sums), ('Sunbelt_Ratio',total_to_sun)]
list3 = [('Year', years),('January',month_1),('Feburary',month_2),('March',month_3),('April',month_4),('May',month_5),('June',month_6),('July',month_7),('August',month_8),('September',month_9),('October',month_10),('November',month_11),('December',month_12)]         
table1 = pd.DataFrame.from_items(list1)   
table2 = pd.DataFrame.from_items(list2) 
table3 = pd.DataFrame.from_items(list3)     
table4 = flights.groupby(['End_State'])[['Flights']].sum()
table5 = (flights.groupby(['Destination'])[['Flights']].sum())
table5 = table5.sort([ 'Flights'], ascending=[0])

flights.to_pickle("flights.pkl")
table1.to_pickle("table1.pkl")
table2.to_pickle("table2.pkl")
table3.to_pickle("table3.pkl")
table4.to_pickle("table4.pkl")
table5.to_pickle("table5.pkl")

#ninety = flights[flights['Year'] == 1990]
#ninety1 = flights[flights['Year'] == 1991]
#ninety2 = flights[flights['Year'] == 1992]
#ninety3 = flights[flights['Year'] == 1993]
#ninety4 = flights[flights['Year'] == 1994]
#ninety5 = flights[flights['Year'] == 1995]
#ninety6 = flights[flights['Year'] == 1996]
#ninety7 = flights[flights['Year'] == 1997]
#ninety8 = flights[flights['Year'] == 1998]
#ninety9 = flights[flights['Year'] == 1999]
#
#print ninety['Distance'].sum() / ninety['Flights'].sum()
#print ninety1['Distance'].sum() / ninety1['Flights'].sum()
#print ninety2['Distance'].sum() / ninety2['Flights'].sum()
#print ninety3['Distance'].sum() / ninety3['Flights'].sum()
#print ninety4['Distance'].sum() / ninety4['Flights'].sum()
#print ninety5['Distance'].sum() / ninety5['Flights'].sum()
#print ninety6['Distance'].sum() / ninety6['Flights'].sum()
