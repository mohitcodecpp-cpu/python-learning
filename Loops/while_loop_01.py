#For taking order and making bill  for restaurant  customers by using while loop
# first we build a menu 
menu ={ "momos" : 100 ,
        "parantha" :40 ,
        "water" : 20 ,
        "coke" : 40,
        "dal" : 80} 

bill=dict()
# taking the input for the number of items 
quantity =int(input("Enter the Number of item in your order = "))
 
# taking the input for order items 
i=0
total=0
while(i<quantity):
    item=input("Enter Your items = ")
    bill.update({item : menu[item.lower()]})
    total+=menu[item]
    i+=1

keys=list(bill.keys())

#to print the order 
m=0
while(m<len(keys)):
    key=keys[m]
    print(key , bill[key])
    m+=1
print("Your Total is " , total)
print("Thanks For buying From our Restaurant")
