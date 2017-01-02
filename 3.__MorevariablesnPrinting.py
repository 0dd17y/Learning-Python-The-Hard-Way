name = '0dd1ty'
age = 23
height = 70 #inches
weight = 74 #kgs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Lets talk about %s." %name
print " He's about %s years old." %age
print "His height is around %d inches tall" %height
print "Actually He's not that heavy, he weighs %d" %weight
print "He's got %s Eyes and %s hair" %(eyes, hair)
print  "His teeth are usually %s depending on the coffee. lol" %teeth

#This line is a little tricky :D
print "If I add %d, %d, and %d then  I get %d " % ( age, height, weight, age + height + weight )