import csv


# Writing to a CSV file
# newline= '' is used to avoid extra new line in csv file

# with open("data.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])


# Reading from a CSV file
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
