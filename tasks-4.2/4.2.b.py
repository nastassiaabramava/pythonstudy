def make_matrix(size, value=0):
    if isinstance(size, tuple):
        n, m = size
    else:
        n = m = size
    return [[value for i in range(n)] for j in range(m)]