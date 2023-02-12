import main;

def test1():
    assert main.average_calories([2200, 2500, 2700, 2900, "done"]) == 2575.0
def test2():
    assert main.average_calories([200, 300, 100, "done"]) == 200.0
def test3():
    assert main.average_calories([1500.2, 1700.3, 1900.4, "done"]) == 1700.3

