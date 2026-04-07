import pandas as pd

df=pd.read_csv("nato_phonetic_alphabet.csv")

df_dict={row.letter:row.code for index,row in df.iterrows()}
print(df_dict)

def getNatoAlphabet():
    try:
        user_name=input("Enter your name: ").upper()
        userNameList = [f"{df_dict[item]}" for item in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        getNatoAlphabet()
    else:
        print(userNameList)


getNatoAlphabet()