def countMax(upRight):
    min_row = float('inf')
    min_col = float('inf')

    for pair in upRight:
        r, c = map(int, pair.split())
        min_row = min(min_row, r)
        min_col = min(min_col, c)

    return min_row * min_col
