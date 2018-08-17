# This orientation session will be tailored to doing some data analysis
# in Python using mainly pandas

# Hurricane Harvey makes landfall 8/25/17
# Hurricane Irma makes landfall 9/10/17
# Hurricane Maria makes landfall 9/20/17

# Fox news vs. CNN or MSNBC

import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime as dt
import getpass

if getpass.getuser()=="nadialucas":
    dbPath = r"/Users/nadialucas/Dropbox/EPIC Predoc Resources/epic_orientation"
else:
	print("please add your machine's directory")


# Set directory paths
dataPath = r"{}/data/Python_R_Puerto_Rico".format(dbPath)

# read in 
media_trump_filename = r"{}/mediacloud_trump.csv".format(dataPath)
google_trends_filename = r"{}/google_trends.csv".format(dataPath)
media_states_filename = r"{}/mediacloud_states.csv".format(dataPath)
media_hurricanes_filename = r"{}/mediacloud_hurricanes.csv".format(dataPath)
tv_hurricanes_filename = r"{}/tv_hurricanes.csv".format(dataPath)
tv_hurricanes_by_network_filename = r"{}/tv_hurricanes_by_network.csv".format(dataPath)

# we create the object media_trump which is an instance of a pandas dataframe
media_trump = pd.read_csv(media_trump_filename)
google_trends = pd.read_csv(google_trends_filename)
media_states = pd.read_csv(media_states_filename)
media_hurricanes = pd.read_csv(media_hurricanes_filename)
tv_hurricanes = pd.read_csv(tv_hurricanes_filename)
tv_hurricanes_by_network = pd.read_csv(tv_hurricanes_by_network_filename)

# For some reason the csvs we read in sometimes has wonky or long variable titles so let's clean those up
# and make sure to get rid of random quotation marks we find.
media_trump = media_trump.rename(columns = {'title:"Puerto Rico"': 'PuertoRico'})
media_trump = media_trump.rename(columns = {'title:"Puerto Rico" AND (title:Trump OR title:President)': 'PuertoRico_Trump'})
media_trump = media_trump.rename(columns = {'title:Florida': 'Florida'})
media_trump = media_trump.rename(columns = {'title:Florida AND (title:Trump OR title:President)': 'Florida_Trump'})
media_trump = media_trump.rename(columns = {'title:Texas': 'Texas'})
media_trump = media_trump.rename(columns = {'title:Texas AND (title:Trump OR title:President)': 'Texas_Trump'})

google_trends = google_trends.rename(columns = {'"Hurricane Harvey": (United States)': 'Harvey_US'})
google_trends = google_trends.rename(columns = {'"Hurricane Irma": (United States)': 'Irma_US'})
google_trends = google_trends.rename(columns = {'"Hurricane Maria": (United States)': 'Maria_US'})
google_trends = google_trends.rename(columns = {'"Hurricane Jose": (United States)': 'Jose_US'})
media_states = media_states.rename(columns = {'"Puerto Rico"': 'Puerto Rico'})

# the dataframe is generally very flexible so in the case we want
# to plot date objects on the x-axis we can remove dates as a vector
# and do a list functional
# pandas is known for its time series functioanlity
google_trends_dates = google_trends['Day']
# the following is a list functional
google_trends_date_objects = [dt.datetime.strptime(d,'%m/%d/%y').date() for d in google_trends_dates]

# then we can plot the x-axis as a date object instead of dealing with a 
# clutter of dates as strings
plt.plot(google_trends_date_objects, google_trends['Harvey_US'], label = "Harvey")
plt.plot(google_trends_date_objects, google_trends['Irma_US'], label = "Irma")
plt.plot(google_trends_date_objects, google_trends['Maria_US'], label = "Maria")
plt.axvline(x=dt.datetime.strptime("9/20/17", '%m/%d/%y').date(), linestyle = 'dotted')
plt.axvline(x=dt.datetime.strptime("8/25/17", '%m/%d/%y').date(), linestyle = 'dotted')
plt.axvline(x=dt.datetime.strptime("9/10/17", '%m/%d/%y').date(), linestyle = 'dotted')
plt.legend(loc='best')

plt.show()


print(media_trump.head())