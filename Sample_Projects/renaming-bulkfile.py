import os

def main():
    i=0
    path = "/home/amit/Pictures/cloudfront/"
    for file in os.listdir(path):
        dest_name = "image" + str(i) + ".png"
        source_name = path + file
        dest_name =  path + dest_name
        os.rename(source_name, dest_name)
        i += 1

main()