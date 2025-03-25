from contextlib import nullcontext


def format_name(first_name,last_name):
    print(f"{first_name.title()} {last_name.title()}")

format_name("smita","KANAWADE")


def is_leap_year(year):
    if year % 4 == 0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")


is_leap_year(int(input("Enter Year")))