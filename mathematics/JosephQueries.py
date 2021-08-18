def query_child(n, pos):
    if n >= pos * 2:
        return pos * 2
    left = n
    while left < pos * 2:
        