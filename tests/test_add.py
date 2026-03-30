from src.main import add

def test_add():
    assert add(3, 2) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0