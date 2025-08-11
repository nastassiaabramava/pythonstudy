def get_dict(text):
    spisok = [a.split('=') for a in text.split(';')]
    return dict(spisok)