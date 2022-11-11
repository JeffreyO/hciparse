"""
This is the fun stuff. The data contained in an HCI record can be parsed using the `bt` submodule.
Parse a HCI event packet. We need to specify HCI type as described in the HCI UART example.
"""
import hciparse.bt.hci as hci
import hciparse.bt.hci_evt as hci_evt

hci_type = 4
hci_data = b'\x13\x05\x01@\x00\x01\x00'

ret = hci.parse(hci_type, hci_data)
print(len(ret))
## 3

evtcode, length, data = ret
print(evtcode)
## 19
print(length)
## 5
print(data)
## b'\x01@\x00\x01\x00'
print(hci_evt.evt_to_str(evtcode))
## EVENT Number_Of_Completed_Packets
