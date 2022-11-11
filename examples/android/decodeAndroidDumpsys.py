# Work In Progress that works. Incomplete implementation to parse the 'dumpsys bluetooth_manager' command on Android 11 devices

from re import search
import os
import base64


def main():
    home = os.path.expanduser("~")
    filename = os.path.join(home, 'tmp', 'BluetoothDumpsys.txt')
    dumpsys = open(filename, 'r')
    
    dumpsys_contents = dumpsys.read()
   #  patternStart = r'--- BEGIN:BTSNOOP_LOG_SUMMARY (* bytes in) ---'
    patternStart = r' bytes in\) ---'
    patternEnd = '--- END:BTSNOOP_LOG_SUMMARY ---'
    pattern = patternStart + '([^&]+?)' + patternEnd
    decodeFile = search(pattern, dumpsys_contents).group(1)
    print(decodeFile)

    decodedFilePath = os.path.join(home, 'tmp', 'BluetoothDumpsysDecoded.txt')
    decodedFileHandle = open(decodedFilePath, 'wb')
    decoded = base64.b64decode(decodeFile)
    decodedFileHandle.write(decoded)
    print(decoded)
    decodedFileHandle.close()

if __name__ == "__main__":
   main()
