from datetime import datetime
import time
shop_items = {}
day_profit = 0
market_items = {}
def addition_items():
    print()
    print('*'*20,'Welcome to MY SUPER MARKET','*'*20)
    print('_'*68)
    global shop_items
    shop_items = {}
    print()
    def add_items_to_shop():
        while True:
            add_items = input('How many items are available to add: ')
            print()
            if add_items.isdigit():
                break
            else:
                print('Input must be numbers.')
                print()
        cnt = 1
        for i in range(0,int(add_items)):
            item = input(f'{cnt}.Enter an item: ').capitalize()
            while True:
                weight = input(f'Enter available weight for {item} in Kgs: ')
                if weight.isdigit():
                    break
                else:
                    print('Input Weight Must be numbers in Kgs.')
                    print()
            while True:
                price = input(f'Set price for {item} in Rs: ')
                if price.isdigit():
                    break
                else:
                    print('Input Price Must be numbers in Rs.')
                    print()
            cnt+=1
            shop_items[item] = [int(weight),int(price)]
            print()
            print(f'Item {item} weight {weight}Kgs price {price}Rs added to shop Succesfully.')
            print()
    return  add_items_to_shop()
addition_items()
def supermarket():
    def available_items():
        print()
        print('*'*15,'Available Items','*'*15)
        print()
        print('   Item',' '*6,'Quantity',' '*4,'Price')
        print('-'*47)
        count_items = 1
        global shop_items
        for i in shop_items:
            print(f'{count_items}.',i,' '*(10-len(i)),shop_items[i][0],'Kgs',' '*5,shop_items[i][1],'Rs')
            count_items+=1
        print('-'*47)
    available_items()
    print()
    customer_database = {}
    cus_needs = ''
    today_profit = 0
    while True:
        print('-'*23)
        print('Select an option: 1 - 3')
        print('-'*23)
        cnt = 0
        for i in shop_items:
            if shop_items[i][0] >= 1:
                cnt+=1
        print('1.Sell\n2.Modify Items\n3.Close the shop')
        print()
        select = int(input('Enter an option: '))
        print()
        cart = {}
        if select == 1:
            available_items()
            print()
            if cnt == 0:
                print('Selling is not available. Becuase items in shop currently out of stcok.\nPlease select 2nd option & Add items to sell')
                time.sleep(3)
                print()
                continue
            while True:
                items_need = input('How many items customer need: ')
                print()
                if items_need.isdigit():
                    break
                else:
                    print('Input must be numbers.')
            condition = False
            while True:
                cus_cnt = 1
                for i in range(0,int(items_need)):
                    while True:
                        cus_item = input(f'Enter an customer item {cus_cnt}: ').capitalize()
                        if cus_item in shop_items:
                            condition = True
                            break
                        else:
                            print(f'{cus_item} not available. Its currently out of stock.')
                            cus_needs+=cus_item+','
                            condition = False
                            print()
                            break
                    while True:
                        if condition == True:
                            cus_weight = input('Enter quantity in Kgs: ')
                            print()
                            if float(cus_weight) <= shop_items[cus_item][0]:
                                shop_items[cus_item][0]-=float(cus_weight)
                                if cus_item in cart:
                                    cart[cus_item][0]+=float(cus_weight)
                                    y = (shop_items[cus_item][1]*float(cus_weight))
                                    cart[cus_item][1] += y
                                    break
                                else:
                                    cart[cus_item] = [float(cus_weight),(shop_items[cus_item][1]*float(cus_weight))]
                                    break
                            else:
                                print(f'{cus_weight}Kgs is not available for {cus_item}')
                                print()
                        else:
                            break
                    cus_cnt+=1
                cus_again = input('Customer want to buy more items ?(yes/no): ').capitalize()
                if cus_again == 'No':
                    break
                elif cus_again == 'Yes':
                    while True:
                        cus_item_cnt = input('Enter how many more items customer need: ')
                        if cus_item_cnt.isdigit():
                            items_need = cus_item_cnt
                            break
                        else:
                            print('Input must be digits.')
                else:
                    print('Input must be Yes or No')
            print()
            name = input('Enter Customer name: ').capitalize()
            print()
            while True:
                print('-'*18)
                print('Select one option:')
                print('-'*18)
                print('1.UPI\n2.Card\n3.Cash')
                pay_mode = int(input('Select an option: '))
                if pay_mode == 1:
                    payment = 'UPI'
                    break
                if pay_mode == 2:
                    payment = 'Card'
                    break
                elif pay_mode == 3:
                    payment = 'Cash'
                    break
                else:
                    print('Enter an input between 1 - 3')
                print()
            print()
            print('='*19,'My Super Market','='*18)
            print()
            print(name,' '*(22-len(name)),datetime.now())
            print('-'*50)
            print('   Item',' '*8,'Quantity',' '*13,'Price')
            print('-'*50)
            print()
            total = 0
            for i in cart:
                total+=cart[i][1]
            t = (8/100)*total
            j = 1
            for i in cart:
                print(f'{j}.',i,' '*(12-len(i)),cart[i][0],'Kgs',' '*15,cart[i][1])
                j+=1
            print('-'*50)
            print(' '*25,'Gst',' '*10,t)
            print(' '*25,'Total',' '*8,total+t)
            print(' '*25,'Payment Mode  ',payment)
            print('-'*50)
            print()
            print('*'*14,'Thanks for Shopping','*'*15)
            print()
            print('*'*14,'Please Visit Again','*'*15)
            today_profit+=(total+t)
            print()
            time.sleep(3)           
        elif select == 2:
            print('What do you want to modify ?')
            print('-'*23)
            print('Select an option: 1 - 3')
            print('-'*23)
            print('1.Add Items\n2.Price of Item\n3.Weight of Item')
            print()
            select_modify = int(input('Select an input: '))
            if select_modify == 1:
                add_items_to_shop()
                available_items()
            elif select_modify == 2:
                while True:
                    available_items()
                    change_item = input('Which item you want to modify: ').capitalize()
                    if change_item in shop_items:
                        break
                    else:
                        print('Item not available. Enter available item in shop to change.')
                while True:
                    replace_price = input(f'Enter a price for {change_item} in RS: ')
                    if replace_price.isdigit():
                        shop_items[change_item][1] = int(replace_price)
                        print()
                        print(f'Item {change_item} to price {int(replace_price)} changed Succesfully.')
                        print()
                        available_items()
                        print()
                        break
                    else:
                        print('Input must be numbers in Rs')
            elif select_modify == 3:
                while True:
                    available_items()
                    change_item = input('Which item you want to modify: ').capitalize()
                    if change_item in shop_items:
                        break
                    else:
                        print('Item not available. Enter available item in shop to change.')
                while True:
                    replace_weight = input(f'Enter a weight for {change_item} in RS: ')
                    if replace_weight.isdigit():
                        shop_items[change_item][0] = int(replace_weight)
                        print()
                        print(f'Item {change_item} to weight {int(replace_weight)} changed Succesfully.')
                        print()
                        available_items()
                        print()
                        break
                    else:
                        print('Input must be numbers in Kgs')
            else:
                print('Input must between 1 - 3')
                print()
                                
        elif select == 3:
            break      
        else:
            print('Please select input between 1 - 3.')
            print()
    if len(cus_needs) == 0:
        cus_needs = 'None'
    print('~'*50)
    print()
    print('-'*50)
    print('Today total Profit is:',today_profit,'Rs')
    print()
    print('Customer needs are:--->',cus_needs)
    print('-'*50)
    print()
    print('~~~~~~~~~~~~~~~~~>Shop is closed<~~~~~~~~~~~~~~~~~')
    print() 
    global day_profit
    day_profit += today_profit
    #market_items.update(shop_items)
print()
while True:
    day_cnt = int(input('Enter days to run market: '))
    for i in range(1,day_cnt+1):
        print('~'*7)
        print('Day:',i)
        print('~'*7)
        print()
        supermarket()
        print(f'Total {i} Day  profit is -',day_profit)    