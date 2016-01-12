__author__ = 'Kaiming'

from os import listdir, path

f = lambda searchdir, filename: [path.join(searchdir, f) for f in listdir(searchdir) if f == filename]

print(f('.', 'bug_fix.py'))
