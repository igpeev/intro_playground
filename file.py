# open(path_and_file, mode, encoding) # mode: read/write/append, binary/text

import sys
# sys.getdefaultencoding()
# 'utf-8'

"""
    r = open for reading (default)
    w = open for writing, truncating the file first
    x = open for exclusive creation, failing if the file already exists
    a = open for writing, appending to the end-of-file if it iexists
    b = binary mode
    t = text mode (default)
    + = open a disk file for updating (reading and writing)
    U = universal lewlines mode (for backward compat; should not be used in new code)
"""

f = open('sampletext.txt', mode='wt', encoding='utf-8')
# f = open('sampletext.txt', mode='rt', encoding='utf-8')
# f = open('sampletext.txt', mode='at', encoding='utf-8')
f.write('some text added\n')
# 32 # <-- the number of chars added
f.read(32)      # the number of chars to read
f.read()        # read all, returns str
f.seek(0)       # move the pointer to position 0
f.readline()    # read a line (the one currently indicated by file-pointer)
f.readlines()   # list of all lines
f.writelines([
    'Hello World!\n',
    'This is a date: 2018-11-23\n',
])

f.close()       # actually saves the changes

# with          # implicitly closes the sequence (or file)
