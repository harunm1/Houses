from cs50 import SQL
from sys import argv, exit


def main():

    if len(argv) != 2:
        print("Insufficient number of arguments")  # prints error if insufficient command line arguments
        exit(1)

    db = SQL("sqlite:///students.db")  # connects to students database
    house = argv[1]
    rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first",
                      house)  # prints roster from house using SQL query
    for row in rows:
        first, middle, last, birth = row["first"], row["middle"], row["last"], row["birth"]
        print(f"{first} {middle + ' ' if middle else ''}{last}, born {birth}")  # prints names and birth years of students


# runs main program
main()