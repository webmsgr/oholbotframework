import ohol
import oholparser
import oholobjects

def test_objects():
    obj = oholobjects.OHOLObjects()
    hatchetname = obj.find("hatchet")[0]
    assert obj.__getattr__(hatchetname) == obj.fromid("71")
