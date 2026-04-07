import random

stu_name=["Alex","Bob","Carol","David","Eve"]
stu_random_score={student:random.randint(1,100) for student in stu_name}

student_score={stu_name:stu_score for stu_name,stu_score in stu_random_score.items() if stu_score>=60}
print(student_score)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result={word:len(word) for word in sentence.split(" ")}

print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:temp for day,temp in weather_c.items()}

print(weather_f)



stu_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}


#Looping through the dictionary
for key,value in stu_dict.items():
    print(key,value)

##Iterate over a pandas dataframe
import pandas as pd
df=pd.DataFrame(stu_dict)

new_df={index:row for index,row in df.iterrows() if row.student=="Angela"}
print(new_df)


