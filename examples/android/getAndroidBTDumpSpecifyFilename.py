"""
Getting the btsnoop log from an android device
You can also specify the output file
"""

import os
from hciparse.android.snoopphone import SnoopPhone

phone = SnoopPhone()
home = os.path.expanduser("~")
dst = os.path.join(home, 'tmp', 'mysnoop.log')
filename = phone.pull_btsnoop(dst)

print(filename)
## /home/joekickass/tmp/mysnoop.log
