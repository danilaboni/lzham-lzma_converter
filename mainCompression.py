import lzham
import os

if not os.path.exists('in'):
    os.mkdir('in')

if not os.path.exists('out'):
    os.mkdir('out')

file_import = input('Enter the name of the file you want to open: ')
file = open(f'in/{file_import}', 'rb').read()

file_export = input('Successfully! Enter the file name to save: ')
cfile = open(f'out/{file_export}', 'wb')

compr_result = lzham.compress(file * 1)
cfile.write(compr_result)