# copy this file to ~/.ipython/profile_default/startup/ and restart jupyer notebook server.

import re
from IPython.core.magic import register_cell_magic

@register_cell_magic
def g_count_magic(line, cell):
    content = re.sub('[^A-za-z0-9\s]', ' ', cell)
    content = re.sub('\s+', ' ', content)
    return len(content.lower().split(' '))