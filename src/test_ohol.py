import ohol
import oholparser
import oholobjects

def test_objects():
    obj = oholobjects.OHOLObjects()
    assert obj.stone_hatchet == obj.byid("71")
