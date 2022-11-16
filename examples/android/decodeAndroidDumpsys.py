# Work In Progress that works partially. Incomplete implementation to parse the 'dumpsys bluetooth_manager' command on Android 11 devices
# I'm not sure what exactly is breaking this, but if someone else can spot it, I'd be appreciative.

from re import search
import os
import base64

def main():
    home = os.path.expanduser("~")
    filename = os.path.join(home, 'tmp', 'BluetoothDumpsys.txt')
    dumpsys = open(filename, 'r')
    
    dumpsys_contents = dumpsys.read()
    # patternStart = r'--- BEGIN:BTSNOOP_LOG_SUMMARY (* bytes in) ---'
    patternStart = r' bytes in\) ---'
    patternEnd = '--- END:BTSNOOP_LOG_SUMMARY ---'
    pattern = patternStart + '([^&]+?)' + patternEnd
    decodeFile = search(pattern, dumpsys_contents).group(1)
    # print(decodeFile)
    rawBase64 = decodeFile.replace('\n', '')
    # print(rawBase64)
    
    decodedFilePath = os.path.join(home, 'tmp', 'BluetoothDumpsysDecoded.txt')
    decodedFileHandle = open(decodedFilePath, 'wb')
    decoded = base64.b64decode(rawBase64, altchars="+/",  validate=True)
    # test1 = base64.b64decode(rawBase64, validate=True)
    # test2 = base64.b64decode(rawBase64, altchars="+/",  validate=True)
    decodedFileHandle.write(decoded)
    decodedFileHandle.close()
    # print(decoded)
    # print(test1 == test2)

if __name__ == "__main__":
   main()
