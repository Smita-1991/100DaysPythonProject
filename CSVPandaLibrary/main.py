# import csv
#
# with open("weather_data.csv","r") as file:
#     data=csv.reader(file)
#     temperature=[]
#     for row in data:
#         if row[1]!='temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data=pandas.read_csv("weather_data.csv")


print(data[data["day"]=="Monday"])
print(type(data))
print(data["temp"])

temp_list=data["temp"].to_list()
print(temp_list)

print(sum(temp_list)/len(temp_list))

print(data["temp"].mean())

print(data["temp"].median())

print(data["temp"].max())

print(data["condition"])

print(data.condition)


#get the row day is which has day is "Monday"
print(data[data["day"]=="Monday"])

#Print the the row which has temperature is maximum
print(data[data["temp"]==data["temp"].max()])

Monday=data[data["day"]=="Monday"]

mon_temp=Monday["temp"].to_list()

mon_temp_F=(int(mon_temp[0])*9/5)+32

print(mon_temp_F)

# Create a dataframe form scratch

data_dict={
    "day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "temp":[12,14,15,14,21,22,24],
    "condition":['Sunny','Rain','Rain','Cloudy','Sunny','Sunny','Sunny']
}

data=pandas.DataFrame(data_dict)
print(data[data["temp"]==21])

data.to_csv("new_data.csv")