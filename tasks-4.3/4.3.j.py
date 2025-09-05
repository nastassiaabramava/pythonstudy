def make_linear(args):
    results = []
    for i in args:
        if isinstance(i, list):
            results.extend(make_linear(i))    #применили функцию к списку в списке, чтобы освободить ее
        else:
            results.append(i)
    return results