import lichess 
import pandas as pd 
import os
from dotenv import load_dotenv

# load content of env
load_dotenv()

# load the token
lichess_token = os.getenv("my_token")

# using token 
req1 = lichess.Client(token=lichess_token)

# get profile data from my personal account
mydata = req1.get_data("Trequartistaa")
mydata_df = pd.json_normalize(mydata).transpose()
print(mydata_df)

# 