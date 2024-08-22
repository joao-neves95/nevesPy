def try_get(target_str: str, index: int, default: str) -> str:
    try:
        return target_str[index]
    except IndexError:
        return default


def is_digit(s: str) -> bool:
    return (s[1:] if s[0] in ('-', '+') else s).isdigit()
