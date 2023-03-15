import os
import random
import string

ALPHA_NUM_CHOICES = f'{string.ascii_uppercase}{string.ascii_lowercase}'

def make_token(n=6): 
    return ''.join(random.choices(ALPHA_NUM_CHOICES, k=n))

def get_filename(path, file_name='') -> str:
    file = file_name.split('.')

    while True:
        token = make_token()
        if file_name !='':
            name = f'{file[0]}_{token}'
            if len(file) >= 1:
                name = f'{name}.{file[len(file)-1]}'
            else:
                name = token
            if not os.path.exists(path / name):
                break
    return path / name