import re

in_file = input().strip()
out_file = input().strip()

with open(in_file) as file_in:
    text = file_in.read()

text = text.replace('\t', '')
text = re.sub(r' {2,}', ' ', text)
text = re.sub(r'\n{2,}', '\n', text)
text = re.sub(r'^\s+|\s+$', '', text, flags=re.MULTILINE)

with open(out_file, "w") as file_out:
    file_out.write(text)
