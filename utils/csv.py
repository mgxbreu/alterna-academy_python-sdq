import csv


def extract_rnc_data():
    rnc_list = []

    with open("rnc_list.csv") as rnc_csv:
        csv_reader = csv.DictReader(rnc_csv)

        for row in csv_reader:
            rnc_list.append(row["rnc"])

    return rnc_list
