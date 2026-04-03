a=int(input("enter your Marks of Maths ="  ))
b=int(input("enter your Marks of Physics ="  ))
c=int(input("enter your Marks of Chemistry ="  ))
sum =(a+b+c) 
percentage = float ((sum/300)*100)
passed = False 

if ( (a/100)*100 >=33 and (b/100)*100 >=33 and (c/100)*100 >=33): 
  passed =True 

if( passed ==True and percentage>=40) :
  print("YOU ARE PASS")
  print(f"percentage = {percentage}" )
else:
  print("YOU ARE FAIL")