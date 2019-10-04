#! /user/bin/env python3
# Converts all objects in the OneLifeData repo into a pickle file containing all information about them, used for bots

import os
import random

def main():
    print("Grabbing submodule")
    os.system("git submodule init")
    os.system("git submodule update")
    print("Reading objects")
    objects = [os.path.join("./OneLifeData/objects/",x) for x in os.listdir("./OneLifeData/objects/")]
    print("Found {} objects".format(len(objects))
    objectobjects = {}
    for i in objects:
          with open(i) as file:
              data = file.read().split("\n")
          name = data.pop(1)
          data = (",".join(data)).split(",")
          notknown = []
          thisobject = {x[0]:x[1] for x in [y.split("=") for y in data if "=" in data else ["hasunknown","true",notknown.append(y)]}
          thisobject["name"] = name
          thisobject["unknown"] = notknown
          objectobjects[thisobject["id"]] = thisobject
if __name__ = "__main__":
    main()
