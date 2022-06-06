details = open("demo.txt", "a")
details.write("\n Add. : India")

#write option will just override the file
details = open("demo.txt", "w")
details.write("\n Add. : India")

#write will also create new file
details = open("demo_new.txt", "w")
details.write("\n Add. : India")

details.close()