import pandas as pd

weather_dict={
    "day":["1/2/2017","1/3/2017","1/4/2017","1/5/2017","1/6/2017","1/7/2017","1/8/2017","1/9/2017","1/10/2017","1/11/2017","1/12/2017","1/13/2017"],
    "city":["New York","New York","New York","New York","Mumbai","Mumbai","Mumbai","Mumbai","Paris","Paris","Paris","Paris"],
    "temperature":[32,36,28,33,90,85,87,92,45,50,54,42],
    "windspeed":[6,7,12,7,5,12,15,5,20,13,8,10],
    "event":["Rain","Sunny","Snow","Sunny","Sunny","Fogy","Fogy","Rain","Sunny","Cloudy","Cloudy","Cloudy"]
}

df=pd.DataFrame(weather_dict)

print(df)
print(df.pivot(index="day",columns="city"))