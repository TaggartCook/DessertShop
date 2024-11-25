import dessert
import receipt

class DessertShop():
    def __init__(self):
        pass

    def user_prompt_candy():
        cn = input("What kind of candy do you want? ")
        while True:
            cw = input("How many pounds do you want? ")
            if cw.isdigit():
                break
        while True:
            cppp = input("How much does it cost per pound? ")
            if cppp.isdigit():
                break
        return dessert.Candy(cn,cw,cppp)

    def user_prompt_cookie():
        cookieitem = []
        con = input("What kind of cookie do you want? ")
        if type.con == str:
            cookieitem.append(con)
        ca = input("How many dozens do you want? ")
        if type.ca == int:
            cookieitem.append(ca)
        cppd = input("How much does it cost per dozen? ")
        if type.cppd == float:
            cookieitem.append(cppd)

    def user_prompt_icecream():
        icecreamitem = []
        icn = input("What kind of icecream do you want? ")
        if type.icn == str:
            icecreamitem.append(icn)
        icsc = input("How many scoops do you want? ")
        if type.icn == int:
            icecreamitem.append(icsc)
        icpps = input("How much does it cost per scoop? ")
        if type.icpps == float:
            icecreamitem.append(icpps)

    def user_prompt_sundae():
        sundaeitem = []
        sn = input("What kind of icecream do you want? ")
        ssc = input("How many scoops do you want? ")
        spps = input("How much does it cost per scoop? ") 
        stn = input("What topping would you like? ")
        stp = input("How much does it cost for the topping? ")       
        pass

def main():
    order1 = dessert.Order()
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