# variables
weight = 41.5
cost = 0

# Ground Shipping
if weight <= 2:
    cost = weight * 1.50 + 20.00
    print(cost)
elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20.00
    print(cost)
elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20.00
    print(cost)
elif weight > 10:
    cost = weight * 4.75 + 20.00
    print(cost)

# Ground Shipping Premium
ground_shipping_premium = 125.00
print(ground_shipping_premium)

# Drone Shipping
if weight <= 2:
    cost = weight * 4.50
    print(cost)
elif weight > 2 and weight <= 6:
    cost = weight * 9.00
    print(cost)
elif weight > 6 and weight <= 10:
    cost = weight * 12.00
    print(cost)
elif weight > 10:
    cost = weight * 14.25
    print(cost)
