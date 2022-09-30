#%%
import pandas as pd
df=pd.read_csv('FoodPrice_in_Turkey.csv')
df.head()

# %%
df.to_excel('demo_FoodPrice.xlsx')
df.to_json('demo_FoodPrice.json',orient='columns')
df.to_hdf('demo_FoodPrice.h5', 'table')
df.to_html('demo_FoodPrice.html')

# %%
