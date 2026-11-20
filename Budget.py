# My Daily Budget Tracker - by Duke
days_worked = 26
daily_income = 600
daily_lunch = 120
daily_saapa = 110
rent = 4000

monthly_income = days_worked * daily_income
monthly_lunch = days_worked * daily_lunch
monthly_saapa = days_worked * daily_saapa
total_expenses = monthly_lunch + monthly_saapa + rent
saving = monthly_income - total_expenses

print(f"Income: {monthly_income} KES")
print(f"Lunch: {monthly_lunch} KES")
print(f"Saapa: {monthly_saapa} KES")
print(f"Rent: {rent} KES")
print(f"Total Expenses: {total_expenses} KES")
print(f"SAVING: {saving} KES")
