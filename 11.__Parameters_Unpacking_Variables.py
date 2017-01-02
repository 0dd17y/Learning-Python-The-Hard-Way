from sys import argv

script, first, second, third = argv

#print "The script is called", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third


sname = raw_input("Do you want to know the script name? \n ENter \"YES\" or \"NO\" \n ")
if sname == "YES":
    print "Your script is called %s ", script
else:
    print "Too bad. Looks like you dont want to know your script name "

