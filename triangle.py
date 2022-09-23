import stdio
import sys

# Accept x (int), y (int), and z (int) as command-line arguments.
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

# Set expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two, and False otherwise.

expr = z <= x+y and x <= y+z and y <= x+z
# Write expr to standard output.

stdio.writeln(expr)
