import csv

def get_books(filename: str, name: str):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='|')

        result = list
        for row in reader:
            if row.__contains__(name):
                result.append(row)

        return result


books = get_books("file.csv", "python")
