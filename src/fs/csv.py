import csv
from typing import Any, Iterable


def write_csv_file(path: str, data: Iterable[Iterable[Any]]):
    """
    Writes a CSV file with the given data.
    If the path does not end with ".csv", it will be appended.
    """
    if path.endswith(".csv") is False:
        path = f"{path}.csv"

    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        file.flush()
        file.close()
