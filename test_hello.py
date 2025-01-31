from hello import add
from hello import subtract
def test_addition():
    assert 2 == add(1,1)

def test_subtraction():
    assert 0 == subtract(2,2)

    