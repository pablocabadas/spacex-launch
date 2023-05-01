import pandas as pd
import numpy as np
from pandas import json_normalize
import requests 
import json
import os
from dotenv import load_dotenv
import time
import sys

sys.argv(get_iss_sl_positions)
src.py(get_iss_sl_positions)

def get_iss_sl_positions(numb_of_samples):
    url = "http://api.open-notify.org/iss-now.json"
    url2 = "https://satellitemap.space/json/sl.json?0.2592483420529641+v1007+19253"
    position_iss = []
    position_sl = []
    location_iss = requests.get(url).json()
    location_sl = requests.get(url2).json()['sats'][1:]
    for i in range(numb_of_samples):

        if location_iss['message'] == 'success':
            time.sleep(2)
            print(i)

            position_iss.append(location_iss['iss_position'])
        if 'id' in location_sl:
            time.sleep(2)
            print(i)
            position_sl.append(location_sl)

        else:
            break


    for i in iss_location:

        if i['latitude']==28.4556:
            print(f'ISS Not Clear')

        if i['longitude']==-80.5278:
            print(f'ISS Not Clear')

        if i['latitude']==28.8960:
            print(f'ISS Not Clear')

        if i['longitude']==-81.1184:
            print(f'ISS Not Clear')

        else:
            print(f'ISS Clear')
            break

    for i in location_sl:

        if i['lat']==28.4556:
            print(f'SL Not Clear')

        if i['lng']==-80.5278:
            print(f'SL Not Clear')

        if i['lat']==28.8960:
            print(f'SL Not Clear')

        if i['lng']==-81.1184:
            print(f'SL Not Clear')

        else:
            print(f'SL Clear')
            break
            
            
    df_iss = pd.DataFrame(position_iss)

    return df_iss, df_sl