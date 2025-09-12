def split_numbers(text):
    text = text.split()
    return tuple(int(x) for x in text)