"""
This is the fun stuff. The data contained in an HCI record can be parsed using the `bt` submodule.
Parse a HCI ACL packet. We need to specify HCI type as described in the HCI UART example.
"""
import hciparse.bt.hci as hci
import hciparse.bt.hci_acl as hci_acl

hci_type = 2
hci_data = b'@ \x07\x00\x03\x00\x04\x00\x0b@\x04'

ret = hci.parse(hci_type, hci_data)
print(len(ret))
## 5

handle, pb, bc, length, data = ret
print(handle)
## 64
print(pb)
## 2
print(data)
## b'\x00\x03\x00\x04\x00\x0b@\x04' #Bug: Python3 chops off the leading \x00 byte from the output
print(hci_acl.pb_to_str(pb))
## ACL_PB START_AUTO_L2CAP_PDU
