import numpy as np

menu={'oniondosa':90,
      'plaindosa':40,
      'ravadosa':75,
      'idli':10,
      'vada':5,
      'poori':30,
      'chapathi':30,
      'pongal':35,
      'tea':25,
      'coffee':35,
      'meals':75}


line = input('enter item with count :').split(" ")

#GET ITEM PRICE
item_price=[]  
for i in range(0,len(line),2):

    if line[i].lower() in menu.keys():
          item_price.append(menu.get(line[i].lower()))

    else:
        
         print(line[i],'is not in menu')
    
#GET ITEM QUATITY 

item_quantity=[]
for j in range(1,len(line),2):
    item_quantity.append(int(line[j]))


if len(item_price) == len(item_quantity) :

    multiplied=list(np.multiply(item_price,item_quantity))
    amount=sum(multiplied)
    gst=(amount/100)*5
    total_bill=amount+gst
    print('Total price(GST inclusive):Rs ',total_bill)

else:
    print("Sorry,Only recipies on the menu !",menu.keys())