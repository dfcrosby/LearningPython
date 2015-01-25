# Exercise 5 - More Variables and Printing
# Print formatters
# 

# Defines variables
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
mheight = height * 2.54 # centimetres
weight = 180 # lbs
mweight = weight / 2.2 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %s inches tall." % height
print "He's %s centimetres tall." % mheight
print "He's %d pounds, heavy." % weight
print "He's %s kilos, heavy." % mweight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get exactly right
print "If I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight)
