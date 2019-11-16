from collections import Counter

def mode(arr):
    n = len(arr)

    data = Counter(arr)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    return float("".join(map(str, mode)))