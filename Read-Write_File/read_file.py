#Open a file in read mode.
details = open("demo.txt", "r")
# This line tells about is file readable in Boolean value.
print(details.readable())

# This line will read all the lines of file.
#print(details.read()) 

#This readline() function , will  only read first line of file.
#print(details.readline())
#print(details.readline())

#Rhis readlines() function, will read  all line amd store them in array.
#print(details.readlines())

#This function will print  index 1 O/P of array.
#print(details.readlines()[1])

#for loop to read each line and print using readline()
for line in details.readlines():
    print(line)

#close the file.
details.close()