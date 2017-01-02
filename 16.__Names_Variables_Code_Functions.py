def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    #we dont need *args, Instead we can actually do this
def print_two_again(arg1,arg2):
    print "This is still the arg1: %r, and this is still the arg2 %r" % (arg1, arg2)
def print_one(arg1):
    print "Your one arg is %r " % arg1

#This one prints nothing.
def printNothing():
    print "Hey, Looks like i got nothing."

print_two("Martin", "Mwanzia")
print_two_again("Martin", "Mwanzia")
print_one ("HelloWorld")