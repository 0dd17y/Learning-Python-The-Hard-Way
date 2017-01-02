from sys import argv            #Import the argv library/module from system

script, filename = argv         #Assign commandline argument to filename

txt = open(filename)            #assign the open fileobject returned from "open" function to txt variable.

print "Heres your file %r:" %filename   #Print  the name of your file that you input through the command line
print txt.read()            #Print the contents of the open file


print "Type the filename again:"            #come on, you know what this does
file_again = raw_input("> ")        #prompt the user for a filename and assign the name to file_again variable
txt_again = open(file_again)               #open the file and assign it to the variableclear
txt.close()                         #This is to close the file
txt_again.close()                   #This one too
print txt_again.read()                  #Print the contents of the file.
