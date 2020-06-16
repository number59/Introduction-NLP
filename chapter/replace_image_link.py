# -*- coding: utf-8 -*-

# Author: zhujp
# Date: 2020/6/16


if __name__ == '__main__':
    old = 'https://github.com/NLP-LOVE/Introduction-NLP/raw/master/img/'
    new = '../img/'
    import os
    dir_path = os.path.dirname(os.path.abspath(__file__))
    for name in os.listdir(dir_path):
        if not name.endswith('.md'):
            continue
        md_path = os.path.join(dir_path, name)
        with open(md_path) as f:
            content = f.read()
        content = content.replace(old, new)
        with open(md_path, 'w') as g:
            g.write(content)

