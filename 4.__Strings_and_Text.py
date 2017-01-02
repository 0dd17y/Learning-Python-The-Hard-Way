x = "There are %d types of people. " %10  #Declaring of x
binary = "binary"           #Declaring of binary
do_not = "don't"        #Declaring of do_not
y = "Those who know %s and those who  %s. " %(binary, do_not)   #This is the string concatenation to add the sentences together.

print x         #printing x
print y     #Printing of y

print "I said: %r " % x         #should print "I said" + x
print "I also said: '%s'. " % y     # should print "I said" + y
hilarious = True      #declaring of hilarious
joke_evaluation = "Isnt that joke so funny?! %r"    #declaring of joke evaluation
print joke_evaluation % hilarious  #print joke_evaluation and pass a parameter to the hanging %r
w = "This is he left side of. . ."  #Declaring of w
e = "a string with a right side"    #Declaring of e
print w + e     #should print the two string in that order.

