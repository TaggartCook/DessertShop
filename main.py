import dessert
import receipt

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
    order1.add(dessert.Candy("Candy Corn", 1.5, .25))
    order1.add(dessert.Candy("Gummy Bears", .25, .35))
    order1.add(dessert.Cookie("Chocolate Chip", 6, 3.99))    
    order1.add(dessert.IceCream("Pistachio", 2, .79))    
    order1.add(dessert.Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))    
    order1.add(dessert.Cookie("Oatmeal Raisin", 2, 3.45))    
        
    for item in order1.order:
        print(item.name)
    #data: list[list[str,int,float]]
    data = []
    data.append(["Item", "Cost", "Tax"])
    for i in order1.order:
        data.append([i.name,round(i.calculate_cost()*100)/100,round(i.calculate_tax()*100)/100])
    data.append(["Order Subtotals",round(order1.order_cost()*100)/100,round(order1.order_tax()*100)/100])
    data.append(["Order Total", round((order1.order_cost() + order1.order_tax())*100)/100, ""])
    data.append(["Total Items in Order","", len(order1)])

    print("Total number of items in order:", len(order1))

    
    receipt.make_receipt(
       data , "receipt.pdf" )

main()