import csv

def main():
    product_num = 0

    products_dict = read_dict("products.csv", product_num)
    request_list = read_request("request.csv")
   


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
    