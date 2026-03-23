import pandas as pd
import numpy as np

weather_dict={
    "day":["1/2/2017","1/3/2017","1/4/2017","1/1/2017","1/2/2017","1/4/2017","1/1/2017","1/2/2017","1/2/2017","1/3/2017","1/4/2017","1/2/2017"],
    "city":["New York","New York","New York","New York","Mumbai","Mumbai","Mumbai","Mumbai","Paris","Paris","Paris","Paris"],
    "temperature":[32,36,28,33,90,85,87,92,45,50,54,42],
    "windspeed":[6,7,12,7,5,12,15,5,20,13,8,10],
    "event":["Rain","Sunny","Snow","Sunny","Sunny","Fog","Fog","Rain","Sunny","Cloudy","Cloudy","Cloudy"]
}


df=pd.DataFrame(weather_dict)
g=df.groupby("city")

for city, city_df in g:
    print(city)
    print(city_df)

print(g.get_group("Mumbai"))
print(g.max())
# df.replace(["noday",0,"no"],np.nan,inplace=True)
# OR
new_df=df.replace({
    'day':'noday',
    'temp':0,
    'condition':'no'
},np.nan_to_num(0),inplace=True)

# new_df.to_excel("Practice.xlsx")
# print(df)
