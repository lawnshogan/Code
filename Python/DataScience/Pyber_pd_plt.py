%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "../Resources/city_data.csv"
ride_data_to_load = "../Resources/ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])
pyber_data_df.head()

#  1. Get the total rides for each city type
type_rides_count = pyber_data_df.groupby(["type"]).count()["ride_id"]
type_rides_count

# 2. Get the total drivers for each city type
type_drivers_sum = city_data_df.groupby(["type"]).sum()["driver_count"]
type_drivers_sum

#  3. Get the total amount of fares for each city type
type_fares_sum = pyber_data_df.groupby(["type"]).sum()["fare"]
type_fares_sum

#  4. Get the average fare per ride for each city type. 
type_avg_fare_ride = pyber_data_df.groupby(["type"]).mean()["fare"]
type_avg_fare_ride

# 5. Get the average fare per driver for each city type. 
driver_avg_fare = type_fares_sum / type_drivers_sum
driver_avg_fare

#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.DataFrame({
    "Total Rides" : type_rides_count,
    "Total Drivers" : type_drivers_sum,
    "Total Fares" : type_fares_sum,
    "Average Fare per Ride" : type_avg_fare_ride,
    "Average Fare per Driver": driver_avg_fare})

pyber_summary_df

#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None
pyber_summary_df

#  8. Format the columns.
pyber_summary_df ["Total Rides"] = pyber_summary_df["Total Rides"].map("{:,.0f}".format)

pyber_summary_df ["Total Drivers"] = pyber_summary_df["Total Drivers"].map("{:,.0f}".format)

pyber_summary_df ["Total Fares"] = pyber_summary_df["Total Fares"].map("${:,.2f}".format)

pyber_summary_df ["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map("${:,.2f}".format)

pyber_summary_df ["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map("${:,.2f}".format)

pyber_summary_df 

# 1. Read the merged DataFrame
pyber_data_df.head(10)

# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.

type_date_count = pyber_data_df.groupby(["type", "date"]).sum()["fare"]
type_date_count

# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()
type_date_count = type_date_count.reset_index()
type_date_count

# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
pivot_table = pd.pivot_table(type_date_count, values='fare', index='date', columns='type')
pivot_table.head(10)

# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
loc_pivot_table_df = pivot_table.loc['2019-01-01':'2019-04-29']
loc_pivot_table_df.head(10)

# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.

loc_pivot_table_df.index = pd.to_datetime(loc_pivot_table_df.index)

# 7. Check that the datatype for the index is datetime using df.info()
loc_pivot_table_df.info()

# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
pivot_table_resample = loc_pivot_table_df.resample('W').sum()
pivot_table_resample.info()

# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 
# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')
pivot_table_resample.plot(figsize=(20,10))
plt.ylabel("Fare ($USD)")
plt.title("Total Fare by City Type")

plt.savefig("Resources/PyBer_fare_summary.png")
plt.legend()