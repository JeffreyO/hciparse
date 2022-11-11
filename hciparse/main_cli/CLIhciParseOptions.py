"""
  usage: hciparse [-h] [-q] [-t] filename

  Parse btsnoop or Apple PacketLogger (.pklg) binary data (similar to wireshark)

  positional arguments:
    filename     path to BTSnoop or Apple PacketLogger file

  options:
    -h, --help   show this help message and exit
    -q, --quiet  don't display header
    -t, --table  print everything in a human readable table
"""
import argparse
from hciparse.logparse.logparse import parse as parse_display_list
from hciparse.main_cli.CLIhciParseTable import main as parse_display_table

def print_hdr():
    """
    Print the script header
    """
    print("")
    print("##############################")
    print("#                            #")
    print("#    btsnoop parser v1.1     #")
    print("#                            #")
    print("##############################")
    print("")

def parse_options():
    parser = argparse.ArgumentParser(prog="hciparse", description="Parse btsnoop or Apple PacketLogger (.pklg) binary data (similar to wireshark)")
    parser.add_argument("filename", help="path to BTSnoop or Apple PacketLogger file")
    parser.add_argument("-q", "--quiet", help="don't display header", action="store_true", default=False)
    parser.add_argument("-t", "--table", help="print everything in a human readable table", action="store_true", default=False)
    arguments = parser.parse_args()
    return arguments

def main_cli():
    args = parse_options()
    if args.quiet == False: print_hdr()
    if args.table == True: parse_display_table(args.filename) # Print out table format
    else: records = print(parse_display_list(args.filename)) # Print out list format
    return 0

if __name__ == "__main__":
    main_cli()
