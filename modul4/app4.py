angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}

angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}

angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755,
}

angajat4 = {
'nume': 'Oana Popa',
'departament': 'HR',
'ID': 1977,
'Salar': 5400,
}

angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900,
}

lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

# Print the name, department and ID of the employees with a salary greater than 5000
for emp in lista_dict:
    if emp["Salar"] > 5000:
        print("Salary amount greater than 5000:",
              emp["nume"], "->", emp["departament"], emp["ID"])

print("")

# Create a list of employees name without the manager
employees = []
for emp in lista_dict:
    if emp["departament"] != "Management":
        employees.append(emp)
print("List of employees without the manager:", employees)

print("")

# Average salary at HR
total = 0
count = 0
for emp in lista_dict:
    if emp["departament"] == "HR":
        total += emp["Salar"]
        count += 1
avg_salary = total / count
print("Average salary at HR department:", avg_salary)

