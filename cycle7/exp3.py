import csv
def read_csv_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

csv_filename = "example.csv"
read_csv_file(csv_filename)
