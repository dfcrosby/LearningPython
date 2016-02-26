# Example 15
#

# from sys import argv
# script, filename = argv

print "Type your filename:"  
filename = raw_input (">")
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input (">")

txt_again = open(file_again)

print txt_again.read()

print "closing txt"
result = txt.close()
print "Closed txt with error: %r" % result

print "closing txt_again"
result1 = txt_again.close()
print "Closed txt_again with error: %r" % result
