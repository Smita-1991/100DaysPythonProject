import pandas as pd

df=pd.read_csv("nato_phonetic_alphabet.csv")

df_dict={row.letter:row.code for index,row in df.iterrows()}
print(df_dict)

user_name=input("Enter your name: ").upper()


userNameList=[f"{item} for {df_dict[item]}" for item in user_name]
print(userNameList)