import os
from dotenv import load_dotenv
import pandas_datareader as pdr

load_dotenv()
key=os.environ.get('TIINGO_API_KEY')
df=pdr.tiingo.TiingoDailyReader('ADBE',api_key=key)

print(df.head())