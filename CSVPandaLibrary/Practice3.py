import pandas as pd

weather_india={
    "city":["Mumbai","Pune","Maharashtra"],
    "temperature":[32,36,28],
    "humidity":[80,60,78]
}

weather_usa={
    "city":["New York","Chicago","Orlando"],
    "temperature":[32,34,29],
    "humidity":[78,63,73]
}

df_india=pd.DataFrame(weather_india)
df_usa=pd.DataFrame(weather_usa)

df=pd.concat([df_india,df_usa],keys=["india","usa"])

print(df)
print(df.loc["india"])


india_temperature={
    "city":["Mumbai","Pune","Maharashtra"],
    "temperature":[32,36,28]
}

usa_humidity={
    "city":["New York","Chicago","Orlando"],
    "humidity":[78,63,73]
}

india_df=pd.DataFrame(india_temperature)
usa_df=pd.DataFrame(usa_humidity)

print(pd.concat([india_df,usa_df],keys=["india","usa"]))
print(pd.concat([india_df,usa_df],keys=["india","usa"],axis=1))


print("##################################")
india_temp=pd.DataFrame({
    "city":["New York","Orlando","Chicago","Michigan"],
    "temperature":[32,36,28,40]
})

usa_hum=pd.DataFrame({
    "city":["New York","Chicago","Orlando","Ohio"],
    "humidity":[78,63,73,67]
})

# Common city
print(pd.merge(india_temp,usa_hum,on="city"))

#left + common  //left join
print(pd.merge(india_temp,usa_hum,on="city",how="left"))

#right + common // right join
print(pd.merge(india_temp,usa_hum,on="city",how="right"))

#right + common // outer join
print(pd.merge(india_temp,usa_hum,on="city",how="outer"))

#indicator from where the data has come
print(pd.merge(india_temp,usa_hum,on="city",how="outer",indicator=True))
