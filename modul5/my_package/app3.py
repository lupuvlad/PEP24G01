from modul4.app6 import medie

name = input("Type the name of the student: ")
grades = input("Type the grades of the student separated by comma: ").replace(" ", "")

grades_list = []
for number in grades.split(","):
    try:
        grades_list.append(float(number))
    except ValueError:
        print(f"{number} is not a grade")

assert grades, "No grades were provided"
print(grades_list)

if medie(grades_list) < 5:
    print(f"{name} didn't promote!")
else:
    print(f"{name} promoted!")
