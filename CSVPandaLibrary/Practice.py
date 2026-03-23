import pandas as pd


def convert_condition_cell(cell):
    if cell=='n.a':
        return 'Sunny'
    return cell

def convert_day_cell(cell):
    if cell=='NA':
        return 'Wednesday'
    return cell

df=pd.read_csv("C:/Users/Owner/Desktop/100DaysPythonProject/CSVPandaLibrary/Practice.csv",
               converters={'condition':convert_condition_cell,
                           'day':convert_day_cell,})

new_df=df.dropna()
print(new_df)


print("Max Temperature is")
print(df[df['temp']==df["temp"].max()])

print(df.shape)

#Print last five entries
print(df.tail())
print(df.tail(1))

#Print the rows from 2 to 4
print(df[2:5])

#Print Everything
print(df[:])

#PRing Column
print(df.columns)

#Print column values
print(df.temp)
# OR
print(df["temp"])

print(df[['day','temp']])

print(df.describe())

print(df[df['temp']>=40])

print(df[df['temp']==df['temp'].max()])

# Remove the original indexes and set new index
print(df.set_index('day',inplace=True))
print(df)
print(df.loc['Wednesday'])

# resetting indexes
print(df.reset_index(inplace=True))
print(df)

# Print the day Wednesday row
print(df.set_index('day',inplace=True))
print(df.loc['Wednesday'])


