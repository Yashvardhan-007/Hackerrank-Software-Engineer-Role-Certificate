def countMax(upRight):
    min_row = float('inf')
    min_col = float('inf')

    for pair in upRight:
        r, c = map(int, pair.split())
        min_row = min(min_row, r)
        min_col = min(min_col, c)

    return min_row * min_col

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    n = int(data[0])
    upRight = data[1:n+1]

    print(countMax(upRight))
