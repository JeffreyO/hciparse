"""
Parsing a btsnoop or pklg capture file
Some of the information in a record can be printed as human readable strings
"""
import os
import hciparse.logparse.logparse as bts

home = os.path.expanduser("~")
filename = os.path.join(home, 'tmp', 'mysnoop.log')

records = bts.parse(filename)

## ...
print(len(records))
## 24246
print(records[0])
## (1, 4, 2, datetime.datetime(2015, 4, 2, 6, 29, 25, 914577), '\x01\x03\x0c\x00')
record = records[0]
seq_nbr = record[0]
pkt_len = record[1]
flags = bts.flags_to_str(record[2])
timestamp = record[3]
data = record[4]
print(seq_nbr)
## 1
print(pkt_len)
## 4
print(flags)
## ('host', 'controller', 'command')
print(timestamp)
## 2015-04-02 06:29:25.914577
print(data)
## b'\x01\x03\x0c\x00'
