def modern_print(text):
    if text not in spisok:
        spisok.append(text)
        print(text)


spisok = []