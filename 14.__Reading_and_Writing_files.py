from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, then hit RETURN."

raw_input("?")

print "Opening the file. . ."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now im going to ask you for three lines"

line1 = raw_input("Line 1: \n")
line2 = raw_input("Line 2: \n")
line3 = raw_input("Line 3: \n")

print "I'm going to write these to the file."



target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target = open(filename, 'r')

print "Your lines have been written to the file. The file is now closed."
print "This is what you wrote to the file."
print target.read()
target.close()