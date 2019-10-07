import ohol
import oholparser
import oholobjects

def test_objects():
    objs = oholobjects.OHOLObjects()
    for obj in objs.nameid:
        print("testing {}...".format(obj),end=" ")
        try:
            assert objs.__getattr__(obj) == objs.byid(objs.nameid[obj])
        except AssertionError as e:
            print("FAIL")
            raise e
            return
        print("OK")
        
