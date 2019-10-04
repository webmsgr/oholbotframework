# Converts all objects in the OneLifeData repo into a pickle file containing all information about them, used for bots
import os

def main():
    print("Grabbing submodule")
    os.system("git submodule init")
    os.system("git submodule update")
    print("Reading objects")
    objects = os.listdir("./OneLifeData/objects/")
    print("Found {} objects".format(len(objects))
    
if __name__ = "__main__":
    main()
