def calculateCost(pizza, toppings, drinks, wings, coupons):
    toppingsPrices = {"pepperoni":1.00, "mushroom":.50, "olive":.50, "anchovy":2.00, "ham":1.50}
    drinksPrices = {"small":2.00, "medium":3.00, "large":3.50, "tub":3.75}
    wingsPrices = {10:5.00, 20:9.00, 40:17.50, 100:48.00}
    tax = .625
    finalCost = 0.00

    for each in pizza: finalCost += 13.00
    for topping in toppings: finalCost += toppingsPrices[topping]
    for drink in drinks: finalCost += drinksPrices[drink]
    for wing in wings: finalCost += wingsPrices[wing]
    for coupon in coupons: finalCost *= coupon
    finalCost += finalCost*tax

    return round(finalCost,2)

usrPizza = []
usrToppings = []
usrDrinks = []
usrWings = []
usrCoupons = []

pizzaInput = int(input("How many pizzas: "))
for each in range(1,pizzaInput+1):
    usrPizza.append("pizza")

toppingsInput = "yeah"
while toppingsInput != "done":
    toppingsInput = input("Toppings: ")
    if toppingsInput != "done": usrToppings.append(toppingsInput)

drinksInput = "yeah"
while drinksInput != "done":
    drinksInput = input("Drink size: ")
    if drinksInput != "done": usrDrinks.append(drinksInput)

wingsInput = "yeah"
while wingsInput != "done":
    wingsInput = input("Amount of wings: ")
    if wingsInput != "done": usrWings.append(int(wingsInput))

couponsInput = "yeah"
while couponsInput != "done":
    couponsInput = input("Coupon percentage: ")
    if couponsInput != "done": usrCoupons.append(int(couponsInput)*.01)

print(calculateCost(usrPizza, usrToppings, usrDrinks, usrWings, usrCoupons))
