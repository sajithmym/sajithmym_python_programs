import random

print('~ '*35)
print('\t - Welcome to Dise Simulator -')
print('~ '*35,'\n')

Choice = input("\n\t* Enter 'o' to Simulate Dise :- ")

while Choice == 'o' or Choice == '':
    Simulate_Number = random.randint(1,6)

    if Simulate_Number == 1:
        print('\n')
        print("\t\t\t----------------")
        print("\t\t\t                ")
        print("\t\t\t       @        ")
        print("\t\t\t                ")
        print("\t\t\t                ")
        print("\t\t\t----------------")
    
    if Simulate_Number == 2:
        print('\n')
        print("\t\t\t----------------")
        print("\t\t\t                ")
        print("\t\t\t      @   @     ")
        print("\t\t\t                ")
        print("\t\t\t                ")
        print("\t\t\t----------------")

    if Simulate_Number == 3:
        print('\n')
        print("\t\t\t----------------")
        print("\t\t\t                ")
        print("\t\t\t   @    @    @  ")
        print("\t\t\t                ")
        print("\t\t\t                ")
        print("\t\t\t----------------")

    if Simulate_Number == 4:
        print('\n')
        print("\t\t\t----------------")
        print("\t\t\t                ")
        print("\t\t\t   @    @    @  ")
        print("\t\t\t     @          ")
        print("\t\t\t                ")
        print("\t\t\t----------------")

    if Simulate_Number == 5:
        print('\n')
        print("\t\t\t----------------")
        print("\t\t\t                ")
        print("\t\t\t   @    @    @  ")
        print("\t\t\t     @     @    ")
        print("\t\t\t                ")
        print("\t\t\t----------------")

    if Simulate_Number == 6:
        print('\n')
        print("\t\t\t----------------")
        print("\t\t\t                ")
        print("\t\t\t   @    @    @  ")
        print("\t\t\t   @    @    @  ")
        print("\t\t\t                ")
        print("\t\t\t----------------")

    Choice = input("\n\t* Enter 'o' to Simulate Dise :- ")

print('\n','~ '*35)
print('\t\t - Done -')
print('~ '*35,'\n')