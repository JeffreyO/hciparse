"""
This is the fun stuff. The data contained in an HCI record can be parsed using the `bt` submodule.
Parse a HCI command packet. We need to specify HCI type as described in the HCI UART  example.
"""
import hciparse.bt.hci as hci
import hciparse.bt.hci_cmd as hci_cmd

hci_type = 1
hci_data = b'\x03\x0c\x00'

opcode, length, data = hci.parse(hci_type, hci_data)

print(opcode)
## 3075
print(length)
## 0
print(data)

print(hci_cmd.cmd_to_str(opcode))
## COMND Reset
