#Fruit shop mini project
#customer side code
fruits=['apple','banana','orange']
quantity=[10,20,5]
price=[350,100,200]
cart=[]
kgs=[]
amount=[]
while True:
    print("FAMOUS FRUIT SHOP")
    print("1.Customer")
    print("2.Shopkeeper")
    print("3.Exit")
    role=int(input("Enter your role: "))
    if role==1:
        while True:
            print("Available Fruits:")
            for f in fruits:
                print(f)
            print('1.Append')
            print('2.Remove')
            print('3.View')
            print('4.Exit')
            choice=int(input("Choose an option:"))
            if choice==1:
                fruit=input("Enter which fruit you want: ")
                if fruit in fruits:
                    q=float(input("Enter how many kgs you want: "))
                    idx=fruits.index(fruit)
                    if q<=quantity[idx]:
                        cart.append(fruit)
                        quantity[idx]=quantity[idx]-q
                        kgs.append(q)
                        amt=q*price[idx]
                        amount.append(amt)
                    else:
                        print("out of stack")
                else:
                    print(fruit,"not available")
            elif choice==2:
                fruit=input("Which fruit you want to remove? ")
                if fruit in cart:
                    a=cart.index(fruit)
                    idx=fruits.index(fruit)
                    re=float(input("How many kgs you want to remove? "))
                    quantity[idx]=quantity[idx]+re
                    kgs[a]=kgs[a]-re
                    amount[a]=amount[a]-re*price[idx]
                else:
                    print(fruit,"is not yet added")
            elif choice==3:
                print("*"*30)
                print("YOUR BILL IS")
                print("*"*30)
                s=0
                for a in range(len(cart)):
                    print(cart[a],end="      ")
                    print(kgs[a],end="      ")
                    print(amount[a],end="      ")
                    s=s+amount[a]
                    print()
                print("*"*30)
                print("Total Payable is:",s)
                print("*"*30)
            elif choice==4:
                print("Exiting..")
                break
            else:
                print("Choose correct option")
#code for shopkeeper
    elif role==2:
        while True:
            for f in fruits:
                print(f)
            print('1.Add')
            print('2.Remove')
            print('3.Modify')
            print('4.Exit')
            choice=int(input("Enter your choice: "))
            if choice==1:
                fr=input("Which fruit you want to add? ")
                if fr in fruits:
                    q=int(input("How many kgs you want to add? "))
                    idx=fruits.index(fr)
                    quantity[idx]=quantity[idx]+q
                    print(quantity)
                else:
                    qu=int(input("How many kgs you want to add?"))
                    pr=int(input("What is the price per kg of added fruit? "))
                    fruits.append(fr)
                    quantity.append(qu)
                    price.append(pr)
                    print(fruits)
                    print(quantity)
                    print(price)
            elif choice==2:
                fri=input("Which fruit you want to remove? ")
                if fri in fruits:
                    idx=fruits.index(fri)
                    quantity.pop(idx)
                    price.pop(idx)
                    fruits.pop(idx)
                    print(fruits)
                    print(quantity)
                    print(price)
                else:
                    print(fri,"is not available")
            elif choice==3:
                fr=input("Which fruit is spoiled? ")
                if fr in fruits:
                    idx = fruits.index(fr)
                    spoiled_qty = int(input("How many kgs spoiled? "))
                    if spoiled_qty <= quantity[idx]:
                        quantity[idx]=quantity[idx]-spoiled_qty
                    if quantity[idx]==0:
                        fruits.pop(idx)
                        quantity.pop(idx)
                        price.pop(idx)
            elif choice==4:
                print('Shopkeeper is Exiting..')
                break
    elif role==3:
        print("Thankyou visit again")
        break
    else:
        print("Choose valid role")
