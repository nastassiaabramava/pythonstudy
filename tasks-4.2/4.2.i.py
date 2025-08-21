def product(*args, **kwargs):
    ans = []
    for name in args:
        letters = 1
        updated = False
        for letter, value in kwargs.items():
            if letter in name:
                letters *= value
                updated = True
        if updated:
            ans.append(letters)
    return tuple(ans)