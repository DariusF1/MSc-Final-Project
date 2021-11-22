''' Forecasting lockdowns'''

import pymysql
import pandas as pd
### time series - statsmodels Seasonality decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
### holt winters & single exponential smoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing   
###double and triple exponential smoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error
import numpy as np
alpha = 0.6

connection = pymysql.connect(host='13.95.205.101',
user='Dawson',
password='123456',
database='crime',
cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "SELECT crime_date, COUNT(*) as CrimeCount FROM crime WHERE lockdown=1 GROUP BY crime_date ORDER BY crime_date;"
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    df = pd.DataFrame(result)

df = df.rename({'CrimeCount' : 'Crime Count', 'crime_date' : 'Year/Month'}, axis=1)    
df['Year/Month'] = pd.to_datetime(df['Year/Month'], errors='coerce')
df.set_index('Year/Month', inplace=True)
df.sort_index(inplace=True)
df['HWES2_ADD'] = ExponentialSmoothing(df['Crime Count'],trend='add',damped_trend=False, seasonal=None).fit().fittedvalues

connection = pymysql.connect(host='13.95.205.101',
user='Dawson',
password='123456',
database='crime',
cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "select crime_date, count(*) AS number FROM window GROUP BY crime_date;"
    cursor.execute(sql)
    result2 = cursor.fetchall()
    connection.commit()
    df2 = pd.DataFrame(result2)
    df2 = df2.rename({'number' : 'Crime Count', 'crime_date' : 'Year/Month'}, axis=1)

df2['Year/Month'] = pd.to_datetime(df2['Year/Month'], errors='coerce')
df2.set_index('Year/Month', inplace=True)
df2['HWES2_ADD'] = ExponentialSmoothing(df2['Crime Count'],trend='add',damped_trend=False, seasonal=None).fit().fittedvalues

df2.update(df)
rms = mean_squared_error(df2['Crime Count'], df2['HWES2_ADD'], squared=False)
print(rms)

df2[['Crime Count','HWES2_ADD']].plot(title='Aggregated Lockdown Damped DES');
