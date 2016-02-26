#Ex15 - Reading Files

# import command line parameters
from sys

# Assign script to the name of script file
# Assign filename to the second argument
# script, filename = argv

print sys.argv

# If argv does not include data file name (sys.argv <2), prompt for it.
# If argv includes data file name assign it to filename.
if len(sys.argv) < 2:
	print "Type the filename:"
	filename = raw_input (">")
else:
	script, filename = sys.argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
