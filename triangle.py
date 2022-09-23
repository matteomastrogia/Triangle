import stdio
import sys

# Accept x (int), y (int), and z (int) as command-line arguments.
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

##-> Sys.argv[...] are strings like "3", "4" and "7".
##   When you calculate x+y ("3" + "4") like you do in line 19, you will get "34".
##   Thats because a string is treated like a "letter" and are concatenate like so.
##   You need to cast the values to an int with int(sys.argv...) so they will be treated like numbers!
print("3"+"4") # this will print 34
print(int("3")+int("4")) # this will print 7

# Set expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two, and False otherwise.

expr = z <= x+y and x <= y+z and y <= x+z
# Write expr to standard output.

stdio.writeln(expr)
