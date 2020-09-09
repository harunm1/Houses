from cs50 import SQL
from sys import argv, exit
import csv


# function seperates name into first, middle(if applicable) and last
def name_seperate(full_name):
    names = full_name.split()
    return names if len(names) >= 3 else [names[0], None, names[1]]


def main():
    if len(argv) != 2:
        print("Insufficient number of arguments")  # prints error if insufficient command line arguments
        exit(1)

    db = SQL("sqlite:///students.db")  # connects to students database

    csv_path = argv[1]
    with open(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)  # reads csv file
        for row in reader:
            names = name_seperate(row["name"])  # seperates first, middle and last names
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       names[0], names[1], names[2], row["house"], row["birth"])  # inserts data into table


# runs main program
main()