#So this is a mini programming challenge i found online. You can find the link below. The book said some practice was neccessary.
#Though rather than just read the code, I decided to try it anyway and see. Looks simple so it should be a breeze through the park.
#http://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import  random
die = [ x for x in range(1, 7)]


def gamestart():
    global die_number
    choice = raw_input("Please enter the number of tmes you wish to spin >>")
    die_number = int(choice)
    assert isinstance(die_number, int)
    print "Good, so you want to roll %d times huh? Okay. " %die_number
    roll_die()

def roll_die():
    global die_number
    print "You rolled the die and here are the results"

    while int(die_number) > 0:
        print " Hey!!! Looks like you just scored a %d" %random.choice(die)
        die_number += -1


gamestart()


