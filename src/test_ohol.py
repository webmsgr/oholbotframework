from __future__ import print_function
import ohol
import oholparser
import oholobjects


def objects(objs=None):
    if objs is None:
        objs = oholobjects.OHOLObjects()
    for obj in objs.nameid:
        print("testing {}...".format(obj),end=" ")
        try:
            assert objs.__getattr__(obj) == objs.byid(objs.nameid[obj])
            objobj = objs.__getattr__(obj)
            assert obj in objs.find(objobj.name[:-2])
            assert objs[obj] == objobj
            for objprop in objobj:
                assert objobj[objprop] == objobj.__getattr__(objprop)
        except AssertionError as e:
            print("FAIL")
            raise e
        print("OK")
    return True
def transitions(trans=None):
    if trans is None:
        trans = oholobjects.OHOLTransitions()
    for tran in trans:
        print("testing {}...".format(tran),end=" ")
        tran = trans[tran]
        for prop in (tran.actor,tran.target,tran.newActor,tran.newTarget):
            try:
                ex = False
                tran.obj.byid(prop) 
            except:
                ex = True
                print("FAIL")
            assert ex == False
        print("OK")
    return True


def test_all():
    print("Grabbing all...")
    objs,trans = oholobjects.graball()
    print("tesing objects")
    assert objects(objs)
    print("testing transitions")
    assert transitions(trans)
