from dessert import IceCream

def test_icecream():
    icecream1 = IceCream("Mint Chip",3,4.10)
    icecream2 = IceCream("Cookie Dough",1,3.75)
    icecream3 = IceCream("Bubble Gum",5,1.00)

    assert icecream1.name == "Mint Chip"
    assert icecream2.name == "Cookie Dough"
    assert icecream3.name == "Bubble Gum"

    assert icecream1.scoop_count == 3
    assert icecream2.scoop_count == 1
    assert icecream3.scoop_count == 5

    assert icecream1.price_per_scoop == 4.10
    assert icecream2.price_per_scoop == 3.75
    assert icecream3.price_per_scoop == 1.00

    assert icecream1.calculate_cost == 12.3

    assert icecream1.calculate_tax == 0.89175