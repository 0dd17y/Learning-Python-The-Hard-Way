#In the last script I wrote out a simple set of tests asking some questions. In this script you will
#ask the user questions and make decisions based on their answers.

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input("> ")

if door == "1":
    print "Theres a giant bear here eating a cheesecake. What do you?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face.  \t Good job!"
    elif bear == "2":
        print "The bear eats your legs off. \t Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away" %bear

elif door == "2":
    print "You stare into the endless abyss at cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. \t Good job! "
    else:
        print "The insanity rots your eyes into a pool of muck. \t Good luck!"

else:
    print "You stumble around and fall on a knife and die. \t Good Job!"




