import re

def my_count_magic(line, cell):
    content = re.sub('[^A-za-z0-9\s]', ' ', cell)
    content = re.sub('\s+', ' ', content)
    return len(content.lower().split(' '))

def load_ipython_extension(ipython):
    ipython.register_magic_function(my_count_magic, 'cell')
