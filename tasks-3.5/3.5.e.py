from sys import stdin
spisok = []
for line in stdin:  
    for word in line.split():
        word_low = word.lower()
        if word_low == word_low[::-1]:
            if word not in spisok:          
                spisok.append(word)
for word in sorted(spisok):
    print(word)
