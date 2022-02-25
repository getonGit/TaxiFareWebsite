import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
#date_time = input('your date/time of travel')
#user_time = input('your time')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
import requests
url = 'https://taxifare.lewagon.ai/predict'


if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(' 🏘️ Maybe you want to use your own API for the prediction, not the one provided by Le Wagon... :100:')


    plat = st.number_input(' 🚋 your pick lat')
    plon = st.number_input('your pick lon')
    dlat = st.number_input('your drop lat 🚲')
    dlon = st.number_input('your drop lon🚋')
    count = st.number_input('no. of passengers')
    from datetime import datetime
    import pytz

    # create a datetime object from the user provided datetime
    pickup_datetime = "2021-05-30 10:12:00"
    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")

    # localize the user datetime with NYC timezone
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
    st.write(type(formatted_pickup_datetime))

    params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=float(plon),
    pickup_latitude=float(plat),
    dropoff_longitude=float(dlat),
    dropoff_latitude=float(dlon),
    passenger_count=int(count))
    import pandas as pd
    df = pd.DataFrame(data = [[40.783282, -73.950655],[40.769802, -73.984365]],columns=['lat', 'lon'])
    st.map(df)



    response = requests.get(url,params).json()
    #st.write(f'{url}?{params}')
    st.write(response)
