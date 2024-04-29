import folium
from folium import plugins
from folium.plugins import HeatMap
# Load data
import pandas as pd
import seaborn as sns
import plotly.express as px
import json
import numpy as np
import os

# remove warnings
import warnings
warnings.filterwarnings("ignore")
# remove pandas warnings
pd.options.mode.chained_assignment = None 

# Re the NYPD policing data
cwd = os.getcwd()
# print(cwd)
parent_dir = os.path.dirname(cwd)
# print(parent_dir)
filename = 'NYPD_Complaint_Map__Year_to_Date.csv'
df = pd.read_csv(filename)

# focus on the offense "harrasment 2"
df_harassment = df[df['OFNS_DESC'] == 'HARRASSMENT 2']

# print(df_harassment.head())

# # conert the date to datetime
df_harassment['CMPLNT_FR_DT'] = pd.to_datetime(df_harassment['CMPLNT_FR_DT'], errors='coerce')
df_harassment['CMPLNT_FR_TM'] = pd.to_datetime(df_harassment['CMPLNT_FR_TM'], errors='coerce')

# # remove "nan" years
df_harassment = df_harassment.dropna(subset=['CMPLNT_FR_DT'])


# # remove the year 1924
df_harassment = df_harassment[df_harassment['CMPLNT_FR_DT'].dt.year != 1924]


# # Exclude all but the columns Latitude', 'Longitude', "CMPLNT_FR_DT", "CMPLNT_FR_TM"]
df_harassment = df_harassment[['Latitude', 'Longitude', "CMPLNT_FR_DT", "CMPLNT_FR_TM"]]
# print(df_harassment.head())



# rename to X and Y
df_harassment = df_harassment.rename(columns={'Latitude': 'Y', 'Longitude': 'X'})

# Extract day of the week and time
df_harassment['weekday'] = df_harassment['CMPLNT_FR_DT'].dt.day_name()
df_harassment['hour'] = df_harassment['CMPLNT_FR_TM'].dt.hour


# Set all coordinates to float
df_harassment['X'] = df_harassment['X'].astype(float)
df_harassment['Y'] = df_harassment['Y'].astype(float)

print(df_harassment.shape)


# def update_heatmap(day, hour):
#     # Filter for the specific day and hour
#     filtered_data = df_harassment[(df_harassment['weekday'] == day) & (df_harassment['hour'] == hour)]

#     # Generate list of [lat, lon] pairs
#     heat_data = [[row['Y'], row['X']] for index, row in filtered_data.iterrows()]

#     # Create a new map
#     heat_map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
#     HeatMap(heat_data, radius=15, blur=5).add_to(heat_map)
    
#     # Save to HTML
#     map_file = "heatmap.html"
#     heat_map.save(map_file)
#     print(f"Heatmap saved to {map_file}. Please open this file in a web browser to view the map.")
#     return heat_map

# # Collect inputs
# day = input("Enter the day of the week (Monday, Tuesday, etc.): ")
# hour = int(input("Enter the hour of the day (0-23): "))
# update_heatmap(day, hour)
