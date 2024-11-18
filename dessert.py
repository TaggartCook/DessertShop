from abc import ABC, abstractmethod
import receipt
class DessertItem(ABC):
    def __init__(self,name):
        self.name = name
        self.tax_percent = 7.25

    @abstractmethod

    def calculate_cost(self):
        pass
    
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent)
        return tax

class Candy(DessertItem):
    def __init__(self,name,candy_weight,price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return cost

class Cookie(DessertItem):
    def __init__(self,name,cookie_quantity,price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        cost = self.cookie_quantity * self.price_per_dozen
        return cost

class IceCream(DessertItem):
    def __init__(self,name,scoop_count,price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
   
    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return cost

class Sundae(IceCream):
    def __init__(self,name,scoop_count,price_per_scoop,topping_name,topping_price):
        super().__init__(name,scoop_count,price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def calculate_cost(self):
        cost = (self.scoop_count * self.price_per_scoop)+(self.topping_price)
        return cost

class Order():
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def add(self,added_item):
        self.order.append(added_item)    

    def order_cost(self):
        total_cost = 0.00
        for i in self.order:
            total_cost += i.calculate_cost()
        return total_cost
    
    def order_tax(self):
        total_tax = 0.00
        for i in self.order:
            total_tax += i.calculate_tax()
        return round(total_tax)

def main():
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    order1.add(Candy("Gummy Bears", .25, .35))
    order1.add(Cookie("Chocolate Chip", 6, 3.99))    
    order1.add(IceCream("Pistachio", 2, .79))    
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))    
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))    
        
    for item in order1.order:
        print(item.name)
    #data: list[list[str,int,float]]
    data = []
    for i in order1.order:
        data.append([i.name,i.calculate_cost(),round(i.calculate_tax())])
    data.append(["Order Subtotals",order1.order_cost,order1.order_tax])
    data.append(["Order Total", order1.order_cost() + order1.order_tax()])


    print("Total number of items in order:", len(order1))

    
    receipt.make_receipt(
        DATA = [ 
            [ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
            [ 
                "16/11/2020", 
                "Full Stack Development with React & Node JS - Live", 
                "Lifetime", 
                "10,999.00/-", 
            ], 
            [ "16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"], 
            [ "Sub Total", "", "", "20,9998.00/-"], 
            [ "Discount", "", "", "-3,000.00/-"], 
            [ "Total", "", "", "17,998.00/-"], 
        ],  )

main()