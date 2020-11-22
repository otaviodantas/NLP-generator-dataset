import csv


def TransformToCSV(data: str) -> None:
    with open("dataset.csv", mode="a+", newline="") as file:
        writer = csv.writer(
            file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow([data])
