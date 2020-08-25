import pandas as pd
import numpy as np
import csv
import json
import datetime
from pandas import DataFrame
from fbprophet import Prophet
from sklearn.metrics import mean_absolute_error

def myconverter(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, datetime.datetime):
        return obj.__str__()

use_cols=['Date','PrimaryType','District']
data = pd.read_csv('/Users/srikaavya/Downloads/CrimeData.csv', usecols=use_cols, iterator=True, chunksize=100000)
data = pd.concat(data, ignore_index=True)
data['Date'] = data['Date'].apply(lambda x: datetime.datetime.strptime(x,"%m/%d/%Y %I:%M:%S %p"))
data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
rm_dist = {1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,24,25}
data = data[data.District.isin(rm_dist)]
data = data[data.Date > '2010-01-31']
data.index = pd.DatetimeIndex(data.Date)
districts = data['District'].unique()
predicted_data = pd.DataFrame()

for district in districts:
    print(district)
    district_data = data[data.District == district]
    data_prophet = district_data.resample('D').size().reset_index(name='Count')
    data_prophet.columns = ['Date', 'Count']
    data_prophet = data_prophet.rename(columns = {'Date':'ds','Count':'y'})
    m = Prophet()
    m.fit(data_prophet)
    future =m.make_future_dataframe(periods = 20)
    forecast = m.predict(future)
    df = forecast[ forecast['ds'] > '2020-04-09']
    df = df[['ds','yhat']].rename(columns={'ds':'Date', 'yhat':'Predicted Values'})
    df['District'] = district  
    predicted_data = predicted_data.append(df)
    
print(predicted_data.tail())


predicted_data.to_csv(r'/Users/srikaavya/PycharmProjects/Diva/Project/static/data/Prediction.csv', index = False, header=True)




#print(data['LocationDescription'].value_counts().iloc[:15].index)
print("2")
print("3")
#print(mean_absolute_error(np.exp(forecast['y']), np.exp(forecast['yhat'])))\



#df.to_csv(r'/Users/srikaavya/Desktop/DIVA/Project/Forecast.csv', index = False, header=True)
#figure = m.plot_components(forecast) 

"""
#print(data.resample('Y').size())
dist_dict={1:"Central", 2:"Wentworth", 3:"Grand Crossing", 4:"South Chicago", 5:"Calumet", 6:"Gresham", 7:"Eaglewood", 8:"Chicago Lawn", 9:"Deering", 10:"Ogden", 11:"Harrison", 12:"Near West", 14:"Shakespeare", 15:"Austin", 16:"Jefferson Park", 17:"Albany Park", 18:"Near North", 19:"Town Hall", 20:"Lincoln", 22:"Morgan Park", 24:"Rogers Park", 25:"Grand Central"}
rm_dist = {1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,24,25}
data = data[data.District.isin(rm_dist)]

slice_pie_data = data[['District', 'LocationDescription']]
slice_pie_data = slice_pie_data.groupby(['District', 'LocationDescription']).size().reset_index(name='counts')
dict = []
list = {}
for crime in slice_pie_data["District"].unique():
    c = slice_pie_data[slice_pie_data.District == crime]['District'].count()
    filtered = slice_pie_data[slice_pie_data.District == crime]
    list['Country'] = crime
    list['Count'] = c
    list['subData'] = []
    sub_list = {}
    max_limit = filtered.counts.nlargest(5).iloc[-1]
    #print(max_limit)
    for row in filtered.itertuples(index=False):
        if  row[2] > max_limit:
            sub_list["LocationDescription"] = row[1]
            sub_list["value"] = row[2]
            list['subData'].append(sub_list)
            sub_list = {}
    dict.append(list)
    list = {}
#fdata = json.dumps(dict, default=myconverter)
#print(fdata)
"""
