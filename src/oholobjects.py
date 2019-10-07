#! /user/bin/env python3
from __future__ import print_function
import os
import glob
import json
import shutil
def bootstrap():
    os.system("git clone https://github.com/jasonrohrer/OneLifeData7/ OneLifeData")
def debootstrap():
    shutil.rmtree('./OneLifeData/')
class OHOLObject():
    def __init__(self,data):
        self.props = data
    def __getattr__(self,prop):
        if prop in self.props:
            return self.props[prop]
        else:
            raise AttributeError("No property named {}".format(prop))
    def __hash__(self):
        return hash(self.props)
    def __repr__(self):
        return "<OHOL Object {}>".format(self.name)
    def __getstate__(self):
        return self.props
    def __setstate__(self,data):
        self.props = data
    def __getitem__(self, item):
        return self.props[item]
    def __iter__(self):
        return iter(self.props)
def sname(name):
    return name.lower().replace(" ","_").replace("#","").replace("+","").replace("-","_").replace("@","any").replace(">","").replace("*","")
class OHOLObjects():
    def __init__(self):
        self.objs = parseObjects()
        for id in self.objs:
            self.objs[id] = OHOLObject(self.objs[id])
        self.nameid = {}
        for obj in self.objs:
            self.nameid[sname(self.objs[obj].name)] = self.objs[obj].id
    def __getattr__(self,name):
        if name in self.nameid:
            return self.objs[self.nameid[name]]
        else:
            raise AttributeError("No object named {}".format(name))
    def __repr__(self):
        return "<All OHOL Objects>"
    def __getstate__(self):
        return (self.objs,self.nameid)
    def __setstate__(self,data):
        self.objs,self.nameid = data
    def byid(self,id):
        return self.objs[id]
    def find(self,objname):
        objname = sname(objname)
        out = {x:self.objs[self.nameid[x]] for x in self.nameid if objname in x}
        return out
    def __getitem__(self, item):
        return self.objs[item]
    def __iter__(self):
        return iter(self.objs)


def graball(trans=None,obj=None):
    out = [trans,obj]
    if trans is None:
        out[0] = parseTransitions()
    if obj is None:
        out[1] = parseObjects()
    return out



def parseTransitions():
    transitions = glob.glob("./OneLifeData/transitions/*.txt")
    obj = {}
    for transition in transitions:
        thisobj = {}
        useLastActor = False
        useLastTarget = False
        if "_LA" in transition:
            useLastActor = True
        elif "_L" in transition:
            useLastTarget = True
        actor,target = os.path.basename(transition).split(".")[0].split("_")[:2]
        thisobj["actor"] = actor
        thisobj["target"] = target
        with open(transition) as fl:
            data = fl.read()
        data = data.split(" ")
        inde = ["newActor","newTarget","autoDecaySeconds","actorMinUseFraction","targetMinUseFraction","reverseUseActorFlag","reverseUseTargetFlag","move","desiredMoveDist","noUseActorFlag","noUseTargetFlag"]
        for dt, ree in enumerate(data):
            thisobj[inde[dt]] = ree
        thisobj["useLastActor"] = useLastActor
        thisobj["useLastTarget"] = useLastTarget
        obj[os.path.basename(transition).split(".")[0]] = thisobj
    return obj
def parseObjects():
    objects = glob.glob("./OneLifeData/objects/*.txt")
    objectobjects = {}
    for i in objects:
        if "nextObjectNumber" in i:
            continue
        with open(i) as file:
            data = file.read().split("\n")
        name = data.pop(1)
        data = (",".join(data)).split(",")
        notknown = []
        thisobject = {x[0]:x[1] for x in [y.split("=") for y in data if "=" in data]}
        thisobject["name"] = name
        thisobject["id"] = thisobject.get("id",os.path.basename(i).split(".")[0])
        thisobject["unknown"] = notknown
        objectobjects[thisobject["id"]] = thisobject
    return objectobjects
