from dessert import Candy

def test_candy():
    candy1 = Candy("Green",3.0,5.25)
    candy2 = Candy("Blue",1.5,9.50)
    candy3 = Candy("Red",1.8,7.75)

    assert candy1.name == "Green"
    assert candy2.name == "Blue"
    assert candy3.name == "Red"

    assert candy1.candy_weight == 3.0
    assert candy2.candy_weight == 1.5
    assert candy3.candy_weight == 1.8

    assert candy1.price_per_pound == 5.25
    assert candy2.price_per_pound == 9.50
    assert candy3.price_per_pound == 7.75

    assert candy1.calculate_cost() == candy1.candy_weight * candy1.price_per_pound

    assert candy1.calculate_tax() == candy1.calculate_cost() * candy1.tax_percent