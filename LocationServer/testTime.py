
import random
import string
import sys
import time
import pickle
import zlib
import bz2
import quicklz
import lz4.block

letters = string.ascii_lowercase

content = ''.join(random.choice(letters) for i in range(1000000))
for i in range(5):
    content = content + content
print("Memory size is : ",sys.getsizeof(content)/1e6)
st = time.time()
content = lz4.block.compress(content.encode('utf-8'),mode='fast')
fl = open('timefile','wb')
pickle.dump(content,fl)
#fl.write(content)
en = time.time()
print("Time taken to compress and dump : ",en-st)
print("Speed is : ",sys.getsizeof(content)/1e6/(en-st))
st = time.time()
fl = open('timefile','rb')
decontent = pickle.load(fl)
decontent = lz4.block.decompress(decontent)
en = time.time()
print("Time taken to read and decompress : ",en-st)
print("Speed is : ",sys.getsizeof(content)/1e6/(en-st))
#content == decontent