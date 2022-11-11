import sys

# import hciparse.logparse.logparse as logparse
from hciparse.logparse.logparse import parse as Parse
from hciparse.logparse.logparse import _read_file_header as Internal_Read_File_Header
from hciparse.logparse.logparse import _validate_btsnoop_header as Internal_Validate_Btsnoop_Header
from hciparse.logparse.logparse import _read_btsnoop_records as Internal_Read_Btsnoop_Records


def main(filename):
#    records = logparse.parse(filename)
    records = Parse(filename)
    print("parse Function:")
    print(records)
    print()
    
    fileHandle = open(filename, "rb")
    print("File Handle:")
    print(fileHandle)
    print()
    with open(filename, "rb") as f:
        print(f)

        fileHeader = Internal_Read_File_Header(f)
        print("_read_file_header Function:")
        print(fileHeader)
        print()

    validatedHeader = Internal_Validate_Btsnoop_Header(fileHeader[0], fileHeader[1], fileHeader[2])
    print("_validate_btsnoop_header Function:")
    print(validatedHeader)
    print()

    btSnoopRecords = Internal_Read_Btsnoop_Records(fileHandle)
    print("_read_btsnoop_records Function:")
    print(btSnoopRecords)
    print()

    print("Printing out map objects from records variable:")
    for record in records:
        print(record[0])
    print()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        sys.exit(-1)
