from typing import Iterable
from pypdf import PdfReader


def read_pdf_file_pages(path: str) -> Iterable[str]:
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)

    allPages = []

    if number_of_pages == 0:
        return allPages

    for pageIndex in range(number_of_pages):
        page = reader.pages[pageIndex]
        allPages.append(page.extract_text())

    return allPages
