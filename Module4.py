# The program asks the user for input N (positive integer) and reads it
print('Enter Positive Integer:')
x = input()
print('Your input is ' + x)

#Then the program asks the user to provide N numbers (one by one) and
#reads all of them (again, one by one)
li= list(map(int, input("Enter multiple values: add space between numbers ").split()))
print("List of input: ", li)

#In the end, the program asks the user for input X (integer) and outputs:
#"-1" if there were no such X among N read numbers, or the index (from 1 to N) of
#this X if the user input it before.
if int(x) in li:
    print(x)
else:
    print(-1)
