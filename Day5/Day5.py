Student_Score=[150,142,185,120,171,203,149,24,59,68,199,78,65,89,86]

max=0

for score in Student_Score:
    if score>max:
        max=score
print(max)

sum=0
for number in range(1,101):
    sum+=number

print(sum)

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")

    else:
        print(number)

