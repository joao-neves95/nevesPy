from typing import Any


def try_get(target: list[Any], index: int, default: Any) -> Any:
    try:
        return target[index]
    except IndexError:
        return default


def table_to_string(table: list[list[str]], column_separator: str) -> str:
    """
    Converts a matrix table into a string, where each row is separated by "\\n"
    """
    return "\n".join((column_separator.join(row) for row in table))
