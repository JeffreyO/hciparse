"""
Getting the btsnoop log from an android device
"""
import os
from hciparse.android.snoopphone import SnoopPhone

phone = SnoopPhone()
filename = phone.pull_btsnoop()

print(filename)
## /tmp/tmp7t971D/btsnoop_hci.log
