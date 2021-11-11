food_file = open('CupcakeInvoices.csv')

for row in food_file:
    print(row)

for row in food_file:
    food = row.split(',')
    print(food[2])

for row in food_file:
    food = row.split(',')
    total = float(food[3]) * float(food[4]) 
    print(total)

total_all = 0
for row in food_file:
    food = row.split(',')
    total = float(food[3]) * float(food[4]) 
    total_all += total
print(total_all)

food_file.close()
