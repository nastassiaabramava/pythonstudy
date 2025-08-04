while (s := input()) != '':
    if not s.startswith('#'):
        if '#' in s:
            k = s.find('#')
            print(s[:k])
        elif '#' not in s:
            print(s) 
