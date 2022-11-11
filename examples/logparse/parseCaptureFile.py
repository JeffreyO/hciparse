"""
Parsing a btsnoop or pklg capture file
"""

import os
import hciparse.logparse.logparse as bts

home = os.path.expanduser("~")
filename = os.path.join(home, 'tmp', 'mysnoop.log')
records = bts.parse(filename)

print(len(records))
# 24246
print(records[0])
## (1, 4, 2, datetime.datetime(2015, 4, 2, 6, 29, 25, 914577), '\x01\x03\x0c\x00')
print(records[-1])
## (24246, 8, 3, datetime.datetime(2015, 4, 2, 9, 9, 57, 655656), '\x04\x13\x05\x01@\x00\x01\x00')
