import pandas as pd 
import numpy as np

df = pd.read_csv('household_power_consumption.txt', delimiter=';')

df.head()

df.columns

'''
Here are the columns that are in the dataset

['Date', 'Time', 'Global_active_power', 'Global_reactive_power',
       'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2',
       'Sub_metering_3'],

'''

# making a new column for the datetime, we will combine the date and time columns to make a new column
df['datetime'] = df['Date'] + ' ' + df['Time']

df.head()


# making a new column that is the index of the datetime column
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.set_index('datetime')
df.head()


# saving this down to a csv file
df.to_csv('household_power_consumption_cleaned.csv')