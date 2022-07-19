# Dominic Docimo
# 7/19/22
# This program will calculate the total cost of 3 items


items = []
count = 0
shipping_cost = 5.99
tax_rate = 1.065

while count < 3:
    name = input("What is the name of the item?")
    price = float(input("What is the price of the item?"))
    items.append((name, price))
    count += 1

print("Here is the list of your items:")

for item in items:
    print(item[0] + ": $" + str(item[1]))

print("-----------------------------------------------------")
subtotal = sum(item[1] for item in items)
print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(round((subtotal * tax_rate) - subtotal, 2)))
print("Shipping: $" + str(shipping_cost))
print("Order total: $" + str(round(subtotal * tax_rate + shipping_cost, 2)))
print("Thanks for shopping!")
