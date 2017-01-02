def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d :" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d " % (a, b)
    return a * b

def divide(a, b):
    print "We are dividing %r with %r" % (a, b)
    return a / b            #try float()

print "Let's do some math with just fuctions!"

age = add(20, 3)
height = subtract(78, 4)
weight = multiply(36, 2)
iq = divide(200, 2)

print "Age: %d, Height: %d, Weight: %id, IQ: %d \n \n" % (age, height, weight, iq,)

#A puzzle for the extra credit, type it in anyway

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, " Can you buy it by hand? "





