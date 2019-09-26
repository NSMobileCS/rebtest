import os
working_dir = os.listdir('.')
for fn in working_dir:
    if fn.endswith('.txt'):
        with open(fn, 'r') as F:
            print(f'{fn} prints: {F.read()}')
