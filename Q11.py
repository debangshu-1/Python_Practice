salary = float(input("Enter the person's salary : "))

if salary < 30000:
    rate = salary * 0.05
elif salary >= 30000 and salary <= 70000:
    rate = salary * 0.15
else:
    rate = salary * 0.25

print(f"Final Tax = {rate : .2f} Rs.")