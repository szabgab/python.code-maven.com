import pickaname
import random

def test_pickaname():
    random.seed(42)
    names = pickaname.select_names('../data/names.txt', 3)
    assert len(names) == 3
    print(names)
