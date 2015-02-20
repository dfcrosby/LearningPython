#Ex15 - Reading Files

# import command line parameters
from sys import argv

# Assign script to the name of script file
# Assign filename to the second argument
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
