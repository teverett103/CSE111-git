import csv
import datetime
# Product fetch and setup
products = {}
totalItems = 0
subtotal = 0.0
total = 0.0
print("Inkom Emporium")
print()
with open("products.csv", "rt") as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        prodNum = row[0]
        prodName = row[1]
        prodPrice = row[2]
        dictionaryUpdate = {prodNum : (prodName, prodPrice)}
        products.update(dictionaryUpdate)
# Request fetch
with open("request.csv", "rt") as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        prodNum = row[0]
        prodQuantity = row[1]
        split = products[prodNum]
        totalItems += int(prodQuantity)
        subtotal += float(split[1]) * float(prodQuantity)
        print(f"{split[0]}: {prodQuantity} @ {split[1]}")
print()
print(f"Number of Items: {totalItems}")
print(f"Subtotal: {subtotal}")
print(f"Sales Tax: {round(subtotal * .06, 2)}")
print(f"Total: {round(subtotal * 1.06, 2)}")
print()
print("Thank you for shopping at the Inkom Emporium.")
print(datetime.datetime.now().strftime("%a %b   %d %I:%M:%S %Y"))
print()

