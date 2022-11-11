"""
  Parse btsnoop or Apple PacketLogger (.pklg) binary data (similar to wireshark). Display as formatted and human readable table.
  usage:
     ./prettyParse.py <filename>
"""

import sys
import binascii
import string
from prettytable import PrettyTable

import hciparse.logparse.logparse as logparse
import hciparse.bt.hci_uart as hci_uart
import hciparse.bt.hci_cmd as hci_cmd
import hciparse.bt.hci_evt as hci_evt
import hciparse.bt.hci_acl as hci_acl
import hciparse.bt.l2cap as l2cap
import hciparse.bt.att as att
import hciparse.bt.smp as smp

def get_rows(records):

    rows = []
    for record in records:

        seq_nbr = record[0]
        time = record[3].strftime("%b-%d %H:%M:%S.%f")

        hci_pkt_type, hci_pkt_data = hci_uart.parse(record[4])
        hci = hci_uart.type_to_str(hci_pkt_type)

        if hci_pkt_type == hci_uart.HCI_CMD:

            opcode, length, data = hci_cmd.parse(hci_pkt_data)
            cmd_evt_l2cap = hci_cmd.cmd_to_str(opcode)

        elif hci_pkt_type == hci_uart.HCI_EVT:

            hci_data = hci_evt.parse(hci_pkt_data)
            evtcode, data = hci_data[0], hci_data[-1]
            
            # if __debug__:
                # print(seq_nbr)
                # print("Debug Stuff evtcode:")
                # print(evtcode)
                # print("Debug Stuff data:")
                # print(data)
                # print("Debug Stuff hci_data[0...2]")
                # print(hci_data[0])
                # print(hci_data[1])
                # print(hci_data[2])
                # print("Debug Stuff orig_len:")
                # print(orig_len)
                # print("Debug Stuff inc_len:")
                # print(inc_len)

            cmd_evt_l2cap = hci_evt.evt_to_str(evtcode)

            # if __debug__:
               # print("Debug stuff cmd_evt_l2cap:")
               # print(cmd_evt_l2cap)
               # print()


        elif hci_pkt_type == hci_uart.ACL_DATA:

            hci_data = hci_acl.parse(hci_pkt_data)
            l2cap_length, l2cap_cid, l2cap_data = l2cap.parse(hci_data[2], hci_data[4])

            if l2cap_cid == l2cap.L2CAP_CID_ATT:

                att_opcode, att_data = att.parse(l2cap_data)
                cmd_evt_l2cap = att.opcode_to_str(att_opcode)
                data = att_data

            elif l2cap_cid == l2cap.L2CAP_CID_SMP:

                smp_code, smp_data = smp.parse(l2cap_data)
                cmd_evt_l2cap = smp.code_to_str(smp_code)
                data = smp_data

            elif l2cap_cid == l2cap.L2CAP_CID_SCH or l2cap_cid == l2cap.L2CAP_CID_LE_SCH:

                sch_code, sch_id, sch_length, sch_data = l2cap.parse_sch(l2cap_data)
                cmd_evt_l2cap = l2cap.sch_code_to_str(sch_code)
                data = sch_data

        data = binascii.hexlify(data)
        data = len(data) > 30 and data[:30] + b"..." or data

        rows.append([seq_nbr, time, hci, cmd_evt_l2cap, data])

    return rows


def main(filename):
    """
    Parse a btsnoop log and print relevant data in a table

    Note: Using an old version of PrettyTable.
    """

    table = PrettyTable(['No.', 'Time', 'HCI', 'CMD/EVT/L2CAP', 'Data'])
    table.align[3] = 'l'
    table.align[4] = 'l'

    records = logparse.parse(filename)
    # print(records)
    rows = get_rows(records)
    # print(rows)
    [table.add_row(r) for r in rows]

    print(table)


def main_cli():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main_cli()
