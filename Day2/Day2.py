print(type(5/3))
print(type(5//3))

# BMI calculator

height=5.4
weight=54

bmi=weight/height
print(int(bmi))
print((round(bmi,3)))

# /////Tip calculator
print("Welcome to the Tip calculator!\n")
total_bill=float(input("What was the total bill?\n"))
tip=float(input("How much tip would you like to give?\n"))
number_of_people=int(input("How many people to split the bill?\n"))
final_tip=total_bill*tip/100
each_person_should_pay=round((total_bill+final_tip)/number_of_people,2)

print(f"Each person should pay {each_person_should_pay}")
