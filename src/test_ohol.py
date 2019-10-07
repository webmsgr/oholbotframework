import ohol
import oholparser
import oholobjects

def test_objects():
    objs = oholobjects.OHOLObjects()
    for obj in objs.nameid:
        print("testing {}".format(obj))
        assert objs.__getattr__(obj) == obj.byid(objs.nameid[obj])
