from dessert import Cookie

def test_cookie():
    cookie1 = Cookie("Chocolate Chip",6,15.00)
    cookie2 = Cookie("Snickerdoodle",8,14.50)
    cookie3 = Cookie("Grasshopper",10,16.50)

    assert cookie1.name == "Chocolate Chip"
    assert cookie2.name == "Snickerdoodle"
    assert cookie3.name == "Grasshopper"

    assert cookie1.cookie_quantity == 6
    assert cookie2.cookie_quantity == 8
    assert cookie3.cookie_quantity == 10

    assert cookie1.price_per_dozen == 15.00
    assert cookie2.price_per_dozen == 14.50
    assert cookie3.price_per_dozen == 16.50

    assert cookie1.calculate_cost() == cookie1.price_per_dozen * cookie1.cookie_quantity

    assert cookie1.calculate_tax() == cookie1.calculate_cost() * cookie1.tax_percent