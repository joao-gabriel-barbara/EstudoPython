# %%
import requests
import pandas as pd
# %%

url = "https://api.opendota.com/api/heroes"

response = requests.get(url)

df = pd.DataFrame(response.json())
df
# %%
df.to_csv("heros_dota.csv", sep=";", index=False)