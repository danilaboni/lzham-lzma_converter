from lzham import LZHAMDecompressor
from lzham import LZHAMCompressor

import lzma
import os

if not os.path.exists('in'):
    os.mkdir('in')

if not os.path.exists('compressed'):
    os.mkdir('compressed')

if not os.path.exists('decompressed'):
    os.mkdir('decompressed')

print('LZHAM(compression) - 1\nLZMA(compression) - 2\n')
print('LZHAM(decompression) - 3\nLZMA(decompression) - 4')

selection = input(f'\nWhich compression algorithm should you use?: ')
	
file_import = input('Enter the name of the file you want to open: ')
file = open(f'in/{file_import}', 'rb').read()

file_export = input('Enter the file name to save: ')
cfile = open(f'compressed/{file_export}', 'wb')
cfile_de = open(f'decompressed/{file_export}', 'wb')

def lzham_compress():
	_lzham = LZHAMCompressor()
	compr_result = _lzham.compress(file * 100)
	cfile.write(compr_result)
	print("Successfully!")

def _lzham_decompress():
	_lzham = LZHAMDecompressor()
	compr_result = _lzham.decompress(file, 40)
	cfile_de.write(compr_result)
	print("Successfully!")	

def lzma_compress():
	with lzma.open(cfile, "w") as f:
		print('Successfully!')
		f.write(file)

def lzma_decompress():
	decomp = lzma.decompress(file)
	cfile_de.write(decomp)
	print('Successfully!')

if selection == '1':
	print('\n[LZHAM] Compression')
	lzham_compress()
	
elif selection == '2':
	print('\n[LZMA] Compression')
	lzma_compress()

elif selection == '3':
	print('\n[LZHAM] Decompression')
	_lzham_decompress()

elif selection == '4':
	print('\n[LZMA] Decompression')
	lzma_decompress()
