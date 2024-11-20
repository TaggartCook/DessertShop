from dessert import Sundae

def test_sundae():
    sundae1 = Sundae("Mint Chip",3,4.10,"Brownie Bites",1.55)
    sundae2 = Sundae("Cookie Dough",1,3.75,"Mini Cookie",3.25)
    sundae3 = Sundae("Bubble Gum",5,1.00,"Gumballs", 2.50)

    assert sundae1.name == "Mint Chip"
    assert sundae2.name == "Cookie Dough"
    assert sundae3.name == "Bubble Gum"

    assert sundae1.scoop_count == 3
    assert sundae2.scoop_count == 1
    assert sundae3.scoop_count == 5

    assert sundae1.price_per_scoop == 4.10
    assert sundae2.price_per_scoop == 3.75
    assert sundae3.price_per_scoop == 1.00

    assert sundae1.topping_name == "Brownie Bites"
    assert sundae2.topping_name == "Mini Cookie"
    assert sundae3.topping_name == "Gumballs"

    assert sundae1.topping_price == 1.55
    assert sundae2.topping_price == 3.25
    assert sundae3.topping_price == 2.50