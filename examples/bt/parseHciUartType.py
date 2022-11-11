"""
This is the fun stuff. The data contained in an HCI record can be parsed using the `bt` submodule.
Parse HCI UART type. This is the first byte of the payload. It tells us what type of HCI packet that is contained in the record.
"""

import hciparse.bt.hci_uart as hci_uart
import hciparse.bt.hci as hci

rec_data = b'\x01\x03\x0c\x00'

hci_type, data = hci_uart.parse(rec_data)

print(hci_type)
## 1
print(data)
## b'\x03\x0c\x00'
print(hci_uart.type_to_str(hci_type))
## HCI_CMD
