from pyqrcode import *
import os

print('~ '*35)
print('\t - Welcome to QR Code Generator -')
print('~ '*35,'\n')
try:
    code = input("\b ---> Enter Code :- ")
    generator = pyqrcode.create(code)
    dd = input("\n --> Enter File Name to save :- ")
    try:
        os.system("mkdir QR_code")
    except:
        pass
    generator.png(f"QR_code/{dd}.png", scale=10)
except Exception as ff:
    print('\n--->',ff,'--->\n')
else:
    print('\n','~ '*35)
    print('\t\t - Done -')
    print('~ '*35,'\n')
