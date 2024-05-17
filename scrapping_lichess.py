import pandas as pd 
import os
from dotenv import load_dotenv
import berserk
# load content of env
load_dotenv()

# load the token
lichess_token = os.getenv("my_token")

# using token 
session = berserk.TokenSession(lichess_token)
client = berserk.Client(session=session)

# get profile data from my personal account
mydata = client.users.get_public_data("Trequartistaa")
mydata_df = pd.json_normalize(mydata).transpose()
#print(mydata_df)

# history 
myhistoy = client.users.get_rating_history("Trequartistaa")
myhistoy_df = pd.json_normalize(myhistoy)
#print(myhistoy_df)

# top 10 
top10_players = client.users.get_all_top_10()

# top players from blitz, rapid, bullet, classical,  ultrabullet
top10_bullet = pd.json_normalize(top10_players, record_path="bullet")
top10_rapid = pd.json_normalize(top10_players, record_path="rapid") 
top10_blitz = pd.json_normalize(top10_players, record_path="blitz") 
top10_classic = pd.json_normalize(top10_players, record_path="classical") 
top10_ultrabullet = pd.json_normalize(top10_players, record_path="ultraBullet") 
 
