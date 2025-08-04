with open(input(), encoding="UTF-8") as file_in:
    words_set1 = file_in.read()
    words1 = set(words_set1.split())
with open(input(), encoding="UTF-8") as file_in:
    words_set2 = file_in.read()
    words2 = set(words_set2.split())
answer = sorted(words1 ^ words2)
with open(input(), "w", encoding="UTF-8") as file_out:
    file_out.write('\n'.join(answer))
