import ohol
import oholparser
import oholobjects

def test_objects():
    obj = oholobjects.OHOLObjects()
    hatchets = obj.find("hatchet")
    for hatchet in hatchets:
        hatchetname = hatchet
    assert obj.__getattr__(hatchetname) == obj.fromid("71")
