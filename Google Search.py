from googlesearch import search

print('~ '*35)
print('\t - Welcome to Google Search -')
print('~ '*35,'\n')

Word = input(" \b Enter to Search :- ")

for i in search(Word,start=0,stop=6):
    print('\n~ ~ ~ ~ ',i)

print('\n','~ '*35)
print('\t\t - Done -')
print('~ '*35,'\n')

input()