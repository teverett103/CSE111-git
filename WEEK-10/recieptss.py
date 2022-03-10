import csv
product = {}

def main():
    product_num = 0

    products_dict = read_dict("products.csv", product_num)
    request_list = read_request("request.csv")
    for key, value in products_dict.items():
        print(key, value)
    
    with open("products.csv") as products:
        with open("request.csv") as request:

            for line in products:
            
                parts = line.split(",")
                product_name = parts[1].strip()
                product_number = parts[0]
                product_price = float(parts[2])
            for line in request:
                parts = line.split(",")  
                quantity = int(parts[1])
                product_number2 = parts[0]
            if product_number == product_number2:
                print(f'{product_name}: {quantity} @ {product_price}')



def read_dict(filename, key_column_index):
    dictionary = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary

def read_request(filename):
    compound_list= []
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        for row_list in reader: 
            compound_list.append(row_list)
    return compound_list

if __name__ == "__main__":
    main()
    