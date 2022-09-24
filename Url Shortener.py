import pyshorteners

print('~ '*35)
print('\t - Welcome to Url Shortener -')
print('~ '*35,'\n')

URL = input("Enter Url :- ")
Execute = pyshorteners.Shortener().tinyurl.short(URL)

print('Short Url is :- ',Execute)

print('\n','~ '*35)
print('\t\t - Done -')
print('~ '*35,'\n')

input()