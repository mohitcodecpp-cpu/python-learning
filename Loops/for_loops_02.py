
#updated order generator for any restaurant using for loops 

menu={"coke" : 40 , "sprit" : 40 , "mango shake" : 80 , "momos" : 50 , "cake" : 120} # this is our menu 
# taking the order from the customer 
order={}
total=0
item_number =int(input("Enter the number Of items you want buy ="))
for i in range (0,item_number):
    item =input("Enter your Item = ")
    a=item.lower()
    quantity =int(input("Enter the quantity of  " + item + ":  " ))
    keyss=item+" * "+str(quantity) 
    valuess=(menu[a])*(quantity)
    order.update({keyss: valuess })
    total+=valuess
    i+=1

print(order)
print("Your Total Is = " , total)
print("thanks For buying from our restaurant :)")
    