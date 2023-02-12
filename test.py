import main;

def test1():
    assert main.average_calories([2200, 2500, 2700, 2900, "done"]) == 2600.0
def test2():
    assert main.average_calories([200, 300, 100, "done"]) == 200.0
def test3():
    assert main.average_calories([1500.25, 1700.50, 1900.75, "done"]) == 1700.5

