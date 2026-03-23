
#List Comprehension

numbers=[1,2,3,4,5]
new_number_list=[number for number in numbers]
print(new_number_list)

name="Smita"
new_List=[letter for letter in name]
print(new_List)


new_number_list=[number*2 for number in range(1,5)]
print(new_number_list)

names=["Alex","Beth","Caroline","Dave","Elanor","Freddie"]

new_name_list=[name.upper() for name in names if len(name)>4]
print(new_name_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers =[number*number for number in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
print(numbers)
result = [num for num in numbers]
print(result)