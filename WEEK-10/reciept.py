
import csv
from datetime import datetime
current_date_and_time = datetime.now()
def read_products(filename, index):
    products = {}
    with open(filename, mode="rt") as product:
        reader = csv.reader(product)
        next(reader)
        for row in reader:
            key = row[index]
            products[key] = [row[1], row[2]]
    return products
def process_request(filename, index, products):
    requested=[]
    x=0
    with open(filename, mode="rt") as request:
        reader = csv.reader(request)
        next(reader)
        """for line in reader:
            requested = products[line[index]]
            print(f"{requested[0]}: {line[1]} @ {requested[1]}")"""
#HERE I TRY TO MAKE A LIST WITH ALL THE INFORMATION ITEM, QUNTIRY AND PRICE
        for line in reader:
            key = line[index]
            req=[products[line[0]][0], line[1], products[line[0]][1]]
            requested.append(req)
            x=x+1
    return requested   
def main():
    try:
        index =0
        detal = 1
        value = 2
        products = read_products("WEEK-10/products.csv", index)
        #for line in products:
            #print(f"{line} {products[line]}")
        index=0
        quantity=1
        requested =process_request("WEEK-10/request.csv", index, products)
        print("Inkom Emporium\n")
        items= ''
        subtotal=0
        #HERE STARTS ALL THE MAGIC (OUTPUT)
        for line in requested:
            print(f"{line[0]}: {line[1]} @ {line[2]}")
            items += int(line[1])
            subtotal += float(line[2])*int(line[1])
        tax = float(subtotal*0.06)
        total = subtotal + tax
        print(f"\nNumber of items: {items}")
        print(f"Subtotal: {subtotal}\nSales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}\n")
        print(f"Thank you for your shoppong at the Inkom Emporium\n{current_date_and_time:%A %I:%M %p}")
        #TEST OF POSIBLE PROBLEMS
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
    except FileNotFoundError as file_not_found_err:
        print(file_not_found_err)



    except PermissionError as perm_err:
        print(f"Error: cannot read from products.csv because you don't have permission.")
if __name__ == "__main__":
    main()

