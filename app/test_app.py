from app.app import add 

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_subtract():
    from app.app import subtract
    assert subtract(5, 3) == 2
