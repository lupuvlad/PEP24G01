import datetime

cnp = input("First 7 digits from CNP: ")

today = datetime.date.today()

gender = cnp[0]
sliced_year = cnp[1:3]
sliced_month = cnp[3:5]
sliced_day = cnp[5:]

if sliced_month[0] == "0":
    birth_month = int(sliced_month[1])
else:
    birth_month = int(sliced_month)

if sliced_day[0] == "0":
    birth_day = int(sliced_day[1])
else:
    birth_day = int(sliced_day)

if len(cnp) == 7:
    if gender == "1" or gender == "2":
        birth_year = int("19" + sliced_year)
    elif gender == "5" or gender == "6":
        birth_year = int("20" + sliced_year)
    else:
        print("You entered a wrong CNP! The first digit must be 1, 2, 5 or 6.")
else:
    print("The number of the digits must be 7!")

user_birthdate = datetime.date(birth_year, birth_month, birth_day)

age = (today - user_birthdate).days / 365.25
# result not good
print(age)

if age > 18:
    print("You are an adult")
else:
    print("You are a child")




