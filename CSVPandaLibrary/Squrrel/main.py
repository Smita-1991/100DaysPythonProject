import pandas

data =pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260319.csv")
print(data)

color_list=data["Primary Fur Color"].to_list()

gray_squirrel=data[data["Primary Fur Color"]=="Gray"]
cinnamon_squirrel=data[data["Primary Fur Color"]=="Cinnamon"]
black_squirrel=data[data["Primary Fur Color"]=="Black"]


gray_count=len(gray_squirrel)
cinnamon_count=len(cinnamon_squirrel)
black_count=len(black_squirrel)


squirrel_dict={
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_count, cinnamon_count, black_count]
}

df=pandas.DataFrame(squirrel_dict)

df.to_csv("new_squirrel_data.csv")
