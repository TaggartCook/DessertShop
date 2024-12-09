import dessert
import receipt

class DessertShop():
    def __init__(self):
        pass

    def user_prompt_candy(self):
        cn = input("What kind of candy do you want? ")
        while True:
            cw = input("How many pounds do you want? ")
            if cw.isdigit():
                cw = int(cw)
                break
        while True:
            cppp = input("How much does it cost per pound? ")
            c2=cppp.split(".")
            if c2[0].isdigit() and (c2[1].isdigit() if len(c2)==2 else True):
                cppp = float(cppp)
                break
        return dessert.Candy(cn,cw,cppp)

    def user_prompt_cookie(self):
        con = input("What kind of cookie do you want? ")
        while True:
            ca = input("How many dozens do you want? ")
            if ca.isdigit():
                ca = int(ca)
                break
        while True:
            cppd = input("How much does it cost per dozen? ")
            c2=cppd.split(".")
            if c2[0].isdigit() and (c2[1].isdigit() if len(c2)==2 else True):
                cppd = float(cppd)
                break
        return dessert.Cookie(con,ca,cppd)

    def user_prompt_icecream(self):
        icf = input("What kind of icecream do you want? ")
        while True:
            icsc = input("How many scoops do you want? ")
            if icsc.isdigit():
                icsc = int(icsc)
                break
        while True:
            icpps = "0"+input("How much does it cost per scoop? ")
            ic2=icpps.split(".")
            if ic2[0].isdigit() and (ic2[1].isdigit() if len(ic2)==2 else True):
                icpps = float(icpps)
                break
        return dessert.IceCream(icf,icsc,icpps)

    def user_prompt_sundae(self):
        sn = input("What kind of icecream do you want? ")
        while True:
            ssc = input("How many scoops do you want? ")
            if ssc.isdigit():
                ssc = int(ssc)
                break
        while True:
            spps = "0"+input("How much does it cost per scoop? ") 
            sp2=spps.split(".")
            if sp2[0].isdigit() and (sp2[1].isdigit() if len(sp2)==2 else True):
                spps = float(spps)
                break
        stn = input("What topping would you like? ")
        while True:
            stp = "0"+input("How much does it cost for the topping? ")       
            st2=stp.split(".")
            if st2[0].isdigit() and (st2[1].isdigit() if len(st2)==2 else True):
                stp = float(stp)
                break
        return dessert.Sundae(sn,ssc,spps,stn,stp)

def main():
    shop = DessertShop()
    order = dessert.Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    done: bool = False

    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',
            '3: Ice Cream',
            '4: Sunday',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()
    for item in order.order:
        print(item)
    #data: list[list[str,int,float]]
    data = []
    data.append(["Item", "Cost", "Tax"])
    for i in order.order:
        data.append([i.name,round(i.calculate_cost()*100)/100,round(i.calculate_tax()*100)/100])
    data.append(["Order Subtotals",round(order.order_cost()*100)/100,round(order.order_tax()*100)/100])
    data.append(["Order Total", round((order.order_cost() + order.order_tax())*100)/100, ""])
    data.append(["Total Items in Order","", len(order)])

    print("Total items in order:", len(order))
    print("Order Subtotal", round(order.order_cost()*100)/100, round(order.order_tax()*100)/100)
    print("Order Total", round((order.order_cost() + order.order_tax())*100)/100,)
    receipt.make_receipt(
       data , "receipt.pdf" )    

main()