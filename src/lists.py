from typing import Any


def try_get(target: list[Any], index: int, default: Any) -> Any:
    try:
        return target[index]
    except IndexError:
        return default


def list_swap(source: list[Any], index_a: int, index_b: int) -> list[Any]:
    """
    Swaps two elements in a list at the specified indices.
    """
    if index_a < 0 or index_b < 0 or index_a >= len(source) or index_b >= len(source):
        raise IndexError("Index out of range")

    source[index_a], source[index_b] = source[index_b], source[index_a]
    return source


def strip_str_list(source: list[str]):
    return [item for item in source if item.strip()]


def remove_in_str_list(source: list[str], sub_str: str):
    return replace_in_str_list(source, sub_str, "")


def replace_in_str_list(source: list[str], sub_str: str, replacer: str):
    return [item.replace(sub_str, replacer) for item in source]


def table_to_string(table: list[list[str]], column_separator: str) -> str:
    """
    Converts a matrix table into a string, where each row is separated by "\\n"
    """
    return "\n".join((column_separator.join(row) for row in table))
