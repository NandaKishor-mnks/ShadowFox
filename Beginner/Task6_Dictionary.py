# 1.Friends name and length
friends = ["Aditya", "Rahul", "Sneha", "Priya", "Kiran"]

friends_with_length = []

for name in friends:
    friends_with_length.append((name, len(name)))

print(friends_with_length)

#2.Expense comparison using dictionaries
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Determine who spent more
if your_total > partner_total:
    print("You spent more money overall")
elif partner_total > your_total:
    print("Your partner spent more money overall")
else:
    print("Both spent the same amount")

# Find category with maximum difference
max_diff = 0
diff_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_diff:
        max_diff = difference
        diff_category = category

print("Highest difference category:", diff_category)
print("Difference amount:", max_diff)
