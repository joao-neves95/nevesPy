import csv
from typing import Any, Iterable


def write_csv_file(path: str, data: Iterable[Iterable[Any]]):
    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        file.flush()
        file.close()
