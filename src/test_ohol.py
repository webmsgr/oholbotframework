from __future__ import print_function
import ohol
import oholparser
import oholobjects


def test_objects():
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

