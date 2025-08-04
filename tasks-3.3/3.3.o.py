{letter: text.lower().count(letter) for letter in sorted(set(text.lower())) if letter.isalpha()}
