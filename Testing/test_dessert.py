from dessert import(DessertItem)

def test_dessertitem():
    d1 = DessertItem("Vanilla")
    d2 = DessertItem("Pie")
    d3 = DessertItem("Cookie")

    assert d1.name == "Vanilla"
    assert d2.name == "Pie"
    assert d3.name == "Cookie"
