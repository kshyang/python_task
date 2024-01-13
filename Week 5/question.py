'''Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used.'''

import sys

path = sys.platform

print(f"The system platform is {path}")

#Question no 2
'''Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).'''
import sys

args = sys.argv[1:]

print(f"There are {len(args)} arguments.")

#Question no 3
'''Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''

import sys

small = sys.argv[1:]
small.sort()

print(f"The smallest is :{small[0]}")

#Question no 4
'''Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.'''


import sys
import requests

url = sys.argv[1]

response = requests.get(url)
print(response)

#Question no 5
'''Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!'''


from statistics import mean
import sys

def maxm(num):
    return max(num)

def minim(num):
    return min(num)

def means(num):
    return mean(num)

if len(sys.argv) == 7:
    vals = sys.argv[1:7]
    vals = [int(x) for x in vals]
    print("max =",maxm(vals))
    print("min =",minim(vals))
    print("mean =",mean(vals))
    
elif len(sys.argv) == 1:
    print("Enter one argument")
    
elif len(sys.argv) > 7:
    print("more arguments then required")

else:
    print("less arguments then required")

#Question no 6
'''Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.'''
   

import sys

file = sys.argv[1]

with open(file, "rt") as source:
    lines = source.read()
    
with open("backup.txt", "w") as copy:
    copy.write(lines)
