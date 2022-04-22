import pandas as pd
import pandas_profiling import ProfileReport

data_frame = pd.read_csv('crime_incident_data2017.csv')

profile = ProfileReport(data_frame, title='Crime Analysis', explorative=True)
