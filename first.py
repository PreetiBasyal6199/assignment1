from tabulate import tabulate
print(" \t \t  Welcome to Australian Coffee Roasters")
while True:
    try:
     n=int(input("Enter the total number of customers:"))
     break
    except:
        print("please enter valid number")
info=[]
for i in range (n):
    name=input("Enter customer name:")
    while True:
        try:
            amount=int(input("Enter the number of coffee beans:")) 
            if amount in range (1,6):
                price = 36
                break
            elif amount in range (6,16):
                price = 34.5
                break
            elif amount in range (16,201):
                price = 32.7
                break
            else:
                print("Invalid Input:Please enter the number between 1 and 200")
                continue
        except:
            print("Please enter the valid integer")

        
    opinion=input("Enter yes/no to indicate whether you are a reseller:")
    total=amount*price
    if opinion=="yes":
        total=total-0.2*total
        print(f"The total sale from {name} is :${total}")
    elif opinion=="no":
        print(f"The total sale from {name} is :${total}")

    print("--------------*****---------------")
    info.append([name,amount,opinion,total])


max_item=max(info, key = lambda x: x[3])
min_item=min(info, key = lambda x: x[3])

print(" \t \t  Summary of sales")

print(tabulate(info, headers=["Name", "No of bags", "Is Reseller", "Total" ]))
        
print(f'The customer spending the most is {max_item[0]} {max_item[3]}')
print(f'The customer spending the minimum is {min_item[0]} {min_item[3]}')