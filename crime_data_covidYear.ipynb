"""
https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
"""
import pandas as pd
import glob
import os
#(1) combine 12 months of crime data 07/2020 - 07/2021
path = r'C:\Users\pigle\OneDrive\Documents\Business Analytics\MSc Project\Raw_Data_covidYear' # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))  # use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f) for f in all_files)
df   = pd.concat(df_from_each_file, ignore_index=True) # doesn't create a list, nor does it append to one
#df.to_excel('combined_file.xlsx')
import folium 
import matplotlib.pyplot as plt
import seaborn as sns 
import webbrowser


#(2) look at null values and remove
plt.figure(figsize=(10,7))
sns.heatmap(df.isnull(), cbar= False, cmap = 'viridis')
#df = df.dropna()
df = df.drop(columns= ['Crime ID', 'Reported by', 'Falls within', 'LSOA code',
                       'Context',], axis=1)

#(3) minor data exploration 
pd.value_counts(df['Location'])[:10]
pd.value_counts(df['Crime type'])[:10]

#(4) location description and semantics
plt.figure(figsize = (15, 10))
sns.countplot(y= 'Crime type', data= df, order= df['Crime type'].value_counts().iloc[:10].index)
liverpool_map = folium.Map(location=[53.400002, -2.983333],
                           zoom_start=11,
                           tiles="CartoDB dark_matter")

locations = df.groupby('LSOA name').first()
new_locations = locations.loc[:, ['Latitude', 'Longitude', 'Location']]
new_locations.head()

#(5) preparing the first map-one location each in a particular community area               
for i in range(len(new_locations)):
    lat = new_locations.iloc[i][0]
    long = new_locations.iloc[i][1]
    popup_text= """LSOA area : {}<br>
                Location : {}<br>"""
    popup_text = popup_text.format(new_locations.index[i],
                new_locations.iloc[i][2]
                )
    
    folium.CircleMarker(location= [lat,long], popup= popup_text, 
                        fill= True).add_to(liverpool_map)
    
#(6) simple criminal rate index DF
    
df['unique_locations'] = list(zip(df['Longitude'], df['Latitude']))
unique_locations = df['unique_locations'].value_counts()


CR_index = pd.DataFrame({"Raw_String" : unique_locations.index, 
                         "ValueCount": unique_locations})
CR_index.index= range(len(unique_locations))
#print(CR_index.head())
temp_index_list = list(CR_index['Raw_String'])

def Location_extractor1(temp_index):
    longitude = []
    latitude = []
    for i in temp_index:
        longitude.append(i[0])
        latitude.append(i[1])
    return longitude, latitude
        
CR_index['LocationCoord_lat'],CR_index['LocationCoord_long'] = Location_extractor1(temp_index_list)

CR_index = CR_index.drop(columns=['Raw_String'], axis = 1)
#print(CR_index)
liverpool_map_CR = folium.Map(location=[53.400002, -2.983333],
                           zoom_start=11,
                           tiles="CartoDB dark_matter")

for i in range(500):
    lat = CR_index['LocationCoord_lat'].iloc[i]
    long = CR_index['LocationCoord_long'].iloc[i]
    radius = CR_index['ValueCount'].iloc[i] / 20
    if CR_index['ValueCount'].iloc[i] > 150:
        color = "#FF4500"
    else:
        color = "#008080"
        
    popup_text = """ Latitude: {}<br>
                Longitude: {}<br>
                Criminal Incidents : {}<br>"""
    popup_text = popup_text.format(long, lat, CR_index['ValueCount'].iloc[i])
    #print([long,lat])
    folium.CircleMarker(location = [long, lat], popup= popup_text,radius = radius, 
                        color = color, fill = True).add_to(liverpool_map_CR)
    
    
os.chdir(r'C:\Users\pigle\OneDrive\Documents\Business Analytics\MSc Project')
 #liverpool_map.save("mymap1.html") #saves map in cwd as html    
liverpool_map_CR.save("mymap2.html")   
webbrowser.open("mymap2.html")
    
                   

#(7) a closer look at violent offences/ sorted array of counts/ overall monthly trend
df_crimetype_violence = df[df['Crime type']=='Violence and sexual offences']
plt.figure(figsize = (11, 7))
sns.countplot(y = df_crimetype_violence['Last outcome category'])

df_crimetype_violence_data=pd.DataFrame({"Counts": 
                                         df_crimetype_violence
                                         ['Last outcome category'].value_counts(),
                                         "Last outcome category":
                                             df_crimetype_violence
                                             ['Last outcome category'].value_counts().index})
df_crimetype_violence_data.reset_index(inplace=True)
df_crimetype_violence_data = df_crimetype_violence_data.drop(columns=['index'],
                                                             axis = 1)
df_crimetype_violence_data.head()   

plt.figure(figsize = (11, 7))
sns.barplot(y="Last outcome category", x = "Counts", data = df_crimetype_violence_data, 
            palette="rocket")

df_crimetype_violence['Month'] = pd.to_datetime(df_crimetype_violence['Month'])
df_crimetype_violence['Month'] = df_crimetype_violence['Month'].apply(lambda x : x.month)
df_cr_violence_months = pd.DataFrame({"violence" : df_crimetype_violence['Month'].value_counts(),
                                      "month" : df_crimetype_violence["Month"].value_counts().index}, 
                                     index = range(12))
df_cr_violence_months.fillna(0, inplace=True)
df_cr_violence_months = df_cr_violence_months.sort_values(['month'], ascending=[1])
                                                          
df_cr_violence_months.head()

plt.figure(figsize = (15,7))
plt.plot(df_cr_violence_months['month'], df_cr_violence_months['violence'], label = 'Monthly Totals')
plt.plot(df_cr_violence_months['month'], df_cr_violence_months['violence'].rolling(window=2).mean(),
         color='red', linewidth=5, label='2-months Moving Average')
plt.title('Violent Crime per Month', fontsize=16)
plt.xlabel('Months')
plt.legend(prop={'size':16})
plt.tick_params(labelsize=16);

#(8) not possible attempt at a daily trend in crime
print(max(df_crimetype_violence['Month']))
print(min(df_crimetype_violence['Month']))
df_crimetype_violence['Month'].iloc[0]

#(9) closer look at burglaries - WIP trying to code unique locations value counts for burglaries 

df_ct_burglary = df[df['Crime type'] == 'Burglary']
unique_locations_burglary = df_ct_burglary['unique_locations'].value_counts()

burglary_index = pd.DataFrame({"Raw strings" : unique_locations_burglary.index,
                               "Value count" : unique_locations_burglary})
burglary_index.index = range(len(unique_locations_burglary))
burglary_index.head()
temp_index_list_b = list(burglary_index['Raw strings'])

burglary_index['LocationCoord_long'], burglary_index['LocationCoord_lat'] = Location_extractor1(temp_index_list_b)
burglary_index = burglary_index.drop(columns=['Raw strings'], axis = 1)

liverpool_map_burglary = folium.Map(location=[53.400002, -2.983333],
                           zoom_start=13,
                           tiles="CartoDB dark_matter")
for i in range(500):
    lat = burglary_index['LocationCoord_lat'].iloc[i]
    long = burglary_index['LocationCoord_long'].iloc[i]
    radius = burglary_index['Value count'].iloc[i] / 1.25
    if burglary_index['Value count'].iloc[i] > 5:
        color = "#FF4500"
    else:
        color = "#008080"
        
    popup_text = """ Latitude: {}<br>
                Longitude: {}<br>
                Burglaries : {}<br>"""
    popup_text = popup_text.format(lat, long, burglary_index['Value count'].iloc[i])
    #print([long,lat])
    folium.CircleMarker(location = [lat, long], popup= popup_text,radius = radius, 
                        color = color, fill = True).add_to(liverpool_map_burglary)

folium.TileLayer('cartodbpositron').add_to(liverpool_map_burglary)

liverpool_map_burglary.save("mymap3.html")   