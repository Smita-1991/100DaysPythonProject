import random

#/// Head or tail
randNumber=random.randint(0,1)
print(randNumber)
if randNumber==0:
    print("Head")
else:
    print("Tail")

#///Get the random element from list
#// option 1
friend_List=['Alice','Bob','Charlie','David','Emanual']
print(random.choice(friend_List))

#// option 1
random_Number=random.randint(0,4)
print(friend_List[random_Number])


