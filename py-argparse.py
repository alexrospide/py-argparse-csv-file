import argparse
import csv
from faker import *
import os

parser = argparse.ArgumentParser()

# Optional Arguments
parser.add_argument("--path", action="store_true", help="print generated file complete path")
parser.add_argument("--encoding",action="store_true", help="enter the encoding of the csv file, default is utf-8")

# Positional Arguments
parser.add_argument("file_name", help="enter a file name")
parser.add_argument("delimiter", help="enter a delimiter character")
parser.add_argument("row_numbers", help="number of lines in the file", type=int)

args = parser.parse_args()

fake = Faker()

# Cabeçalho do CSV
header = ["owner_name", "email", "month_quota", "start_date"]

data = []

r_numbers = args.row_numbers
delimiter = args.delimiter

file_name = args.file_name + ".csv"

if args.encoding:
    encoding = input("Enter the encoding of the csv file: ")
else:
    encoding = "utf-8"


for _ in range(r_numbers):
    month_quota = fake.random.randint(1000, 5000)
    start_date = fake.date_this_decade()
    owner_name = fake.name()
    email = fake.email()

    row = [owner_name, email, month_quota, start_date]
    data.append(row)

with open(file_name, mode="w", newline="", encoding=encoding) as file:
    writer = csv.writer(file, delimiter=delimiter)
    writer.writerow(header)
    writer.writerows(data)

print(f"The CSV file '{file_name}'was generated successfully")

if args.path:
    file_path = os.path.abspath(file_name)
    print(f"the file was generated on this path: \n{file_path}")
