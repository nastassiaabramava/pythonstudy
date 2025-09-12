lambda x: (''.join(i for i in x[0].lower() if i.isalpha()), sum(x[1]) if isinstance(x[1], (list, tuple)) else x[1])

