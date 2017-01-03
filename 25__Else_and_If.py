#A simple exercise to understand the introduction to if and else statements.

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"

if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print " We still cant decide"

if people > buses:
    print "Alright, Lets just take the buses"
else:
    print "Fine! Let's stay at home then."