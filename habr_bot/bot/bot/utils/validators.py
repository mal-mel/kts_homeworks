def validate_time(t: str) -> bool:
    st = t.split(":")
    if len(st) == 2:
        if len(st[0]) == 2 and len(st[1]) == 2:
            return st[0].isdigit() and st[1].isdigit()
    return False
